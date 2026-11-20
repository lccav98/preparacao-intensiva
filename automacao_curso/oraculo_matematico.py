#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Oraculo Matematico Simbolico e Numerico Exato (Python stdlib puro: fractions + ast + math)
para avaliacao deterministica das respostas manuscritas/OCR de MAT121 (Matrizes e Vetores).
"""

import ast
import math
import re
import unicodedata
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple


_FUNCOES_SEGURAS = {
    "sqrt": math.sqrt,
    "abs": abs,
    "sin": math.sin,
    "sen": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "acos": math.acos,
    "arccos": math.acos,
    "asin": math.asin,
    "arcsen": math.asin,
    "atan": math.atan,
    "arctan": math.atan,
    "raiz": math.sqrt,
}

_CONSTANTES_SEGURAS = {
    "pi": math.pi,
}


def remover_acentos(txt: str) -> str:
    nfkd = unicodedata.normalize("NFKD", str(txt or ""))
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch))


def _converter_latex_basico(expr: str) -> str:
    s = str(expr or "").strip()
    s = s.replace("$", " ")
    s = s.replace("−", "-").replace("–", "-").replace("×", "*").replace("·", "*").replace("÷", "/")
    s = s.replace("\\cdot", "*").replace("\\times", "*").replace("\\div", "/")
    s = s.replace("\\left", "").replace("\\right", "")
    s = s.replace("\\pi", "pi").replace("π", "pi")
    s = s.replace("√", "sqrt")

    # \frac{a}{b} (suporta até 3 niveis aninhados simples)
    for _ in range(4):
        novo = re.sub(
            r"\\(?:d|t)?frac\s*\{([^{}]+)\}\s*\{([^{}]+)\}",
            r"((\1)/(\2))",
            s,
        )
        if novo == s:
            break
        s = novo

    # \sqrt{x} -> sqrt(x)
    for _ in range(3):
        novo = re.sub(r"\\?sqrt\s*\{([^{}]+)\}", r"sqrt(\1)", s)
        if novo == s:
            break
        s = novo

    # \operatorname{sen} ou \sin, \cos, etc.
    s = re.sub(r"\\operatorname\{([a-zA-Z]+)\}", r"\1", s)
    s = re.sub(r"\\(sin|cos|tan|sen|arccos|acos|arcsen|asin|arctan|atan)", r"\1", s)
    s = re.sub(r"\\hat\s*\{\s*\\?(?:imath|i)\s*\}", "i", s)
    s = re.sub(r"\\hat\s*\{\s*\\?(?:jmath|j)\s*\}", "j", s)
    s = re.sub(r"\\hat\s*\{\s*\\?k\s*\}", "k", s)
    s = s.replace("\\imath", "i").replace("\\jmath", "j")
    s = s.replace("{", "(").replace("}", ")")
    return s


def _normalizar_expr_python(expr: str) -> str:
    s = _converter_latex_basico(expr)
    # Virgula decimal brasileira entre digitos (ex: 3,5 -> 3.5), sem quebrar listas/vetores com espaco
    s = re.sub(r"(?<=\d),(?=\d)", ".", s)
    # Remover unidade de graus ou texto de grau
    s = re.sub(r"\s*(?:°|graus?|rad|u\.c\.|u\.a\.|u\.v\.)\b", "", s, flags=re.IGNORECASE)
    s = s.replace("°", "")
    s = s.replace("^", "**")
    # Multiplicacao implicita: 2x -> 2*x, 2sqrt(3) -> 2*sqrt(3), 2(x+1) -> 2*(x+1), )x -> )*x, )( -> )*(
    s = re.sub(r"(\d)\s*(?=[a-zA-Z(])", r"\1*", s)
    s = re.sub(r"\)\s*(?=[a-zA-Z0-9(])", r")*", s)
    s = re.sub(r"\b([abcdkmnpqrstwxyz])\s*(?=\()", r"\1*", s, flags=re.IGNORECASE)
    return s.strip()


def _eval_ast_node(node: ast.AST, vars_map: Dict[str, float], modo_fraction: bool) -> Any:
    if isinstance(node, ast.Expression):
        return _eval_ast_node(node.body, vars_map, modo_fraction)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            if modo_fraction:
                if isinstance(node.value, int):
                    return Fraction(node.value, 1)
                return Fraction(str(node.value))
            return float(node.value)
        raise ValueError(f"Constante invalida: {node.value!r}")

    if isinstance(node, ast.Name):
        name = node.id.lower()
        if name in vars_map:
            val = vars_map[name]
            return Fraction(val) if (modo_fraction and not isinstance(val, Fraction)) else (val if isinstance(val, Fraction) and modo_fraction else float(val))
        if name in _CONSTANTES_SEGURAS and not modo_fraction:
            return _CONSTANTES_SEGURAS[name]
        raise ValueError(f"Identificador desconhecido: {node.id}")

    if isinstance(node, ast.UnaryOp):
        v = _eval_ast_node(node.operand, vars_map, modo_fraction)
        if isinstance(node.op, ast.UAdd):
            return +v
        if isinstance(node.op, ast.USub):
            return -v
        raise ValueError("Operador unario nao permitido.")

    if isinstance(node, ast.BinOp):
        left = _eval_ast_node(node.left, vars_map, modo_fraction)
        right = _eval_ast_node(node.right, vars_map, modo_fraction)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            if right == 0:
                raise ZeroDivisionError("Divisao por zero.")
            return left / right
        if isinstance(node.op, ast.Pow):
            if modo_fraction:
                if right.denominator != 1 or abs(right.numerator) > 20:
                    raise ValueError("Expoente nao inteiro em modo exato.")
                return left ** right.numerator
            return left ** right
        raise ValueError("Operador binario nao permitido.")

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Chamada de funcao invalida.")
        fn_name = node.func.id.lower()
        if fn_name not in _FUNCOES_SEGURAS or len(node.args) != 1 or node.keywords:
            raise ValueError(f"Funcao nao permitida: {fn_name}")
        if modo_fraction:
            raise ValueError("Funcao real exige avaliacao em ponto flutuante.")
        arg = float(_eval_ast_node(node.args[0], vars_map, False))
        return float(_FUNCOES_SEGURAS[fn_name](arg))

    raise ValueError(f"Expressao AST nao permitida: {type(node).__name__}")


def avaliar_escalar(
    expr: Any,
    vars_map: Optional[Dict[str, Any]] = None,
) -> Tuple[Optional[Fraction], float]:
    """
    Avalia expressao escalar retornando (Fraction_exata_ou_None, valor_float).
    Lanca ValueError se a expressao nao puder ser avaliada.
    """
    if isinstance(expr, Fraction):
        return expr, float(expr)
    if isinstance(expr, int):
        return Fraction(expr, 1), float(expr)
    if isinstance(expr, float):
        return None, expr

    s = str(expr or "").strip()
    if not s:
        raise ValueError("Expressao escalar vazia.")

    # Remover prefixos do tipo "det(A) =", "x =", "area =", "d =" se houver um unico '='
    if "=" in s and not any(op in s for op in ["==", "<=", ">="]):
        partes_eq = [p.strip() for p in s.split("=")]
        # Usa o lado direito se o lado esquerdo parecer rotulo
        if len(partes_eq) >= 2 and len(partes_eq[-1]) > 0:
            s = partes_eq[-1]

    norm = _normalizar_expr_python(s)
    if not norm:
        raise ValueError("Expressao escalar vazia apos normalizacao.")

    tree = ast.parse(norm, mode="eval")
    vmap = {k.lower(): v for k, v in (vars_map or {}).items()}

    frac_val: Optional[Fraction] = None
    try:
        frac_val = _eval_ast_node(tree, vmap, True)
        if not isinstance(frac_val, Fraction):
            frac_val = Fraction(frac_val)
    except ZeroDivisionError:
        raise
    except Exception:
        frac_val = None

    float_val = float(_eval_ast_node(tree, vmap, False))
    if math.isnan(float_val) or math.isinf(float_val):
        raise ValueError("Valor numerico invalido (NaN/Inf).")
    return frac_val, float_val


def _iguais_escalar(a: Any, b: Any, tol: float = 1e-3) -> bool:
    fa, va = avaliar_escalar(a)
    fb, vb = avaliar_escalar(b)
    if fa is not None and fb is not None:
        return fa == fb
    return abs(va - vb) <= tol * max(1.0, abs(vb))


def _separar_nivel_zero(texto: str, seps: str = ",;") -> List[str]:
    """Divide texto nos separadores informados apenas no nivel 0 de (), [] e {}."""
    itens: List[str] = []
    atual: List[str] = []
    p_depth = 0
    b_depth = 0
    c_depth = 0
    for ch in texto:
        if ch == "(":
            p_depth += 1
        elif ch == ")" and p_depth > 0:
            p_depth -= 1
        elif ch == "[":
            b_depth += 1
        elif ch == "]" and b_depth > 0:
            b_depth -= 1
        elif ch == "{":
            c_depth += 1
        elif ch == "}" and c_depth > 0:
            c_depth -= 1
        if ch in seps and p_depth == 0 and b_depth == 0 and c_depth == 0:
            tok = "".join(atual).strip()
            if tok:
                itens.append(tok)
            atual = []
        else:
            atual.append(ch)
    tok = "".join(atual).strip()
    if tok:
        itens.append(tok)
    return itens


def _parse_conjunto_numeros(texto: Any) -> List[Tuple[Optional[Fraction], float]]:
    if isinstance(texto, list):
        return [avaliar_escalar(x) for x in texto]

    s = str(texto or "").strip()
    if "=" in s:
        # Ex: "m = +-9" ou "r = 0 ou r = 2"
        s = re.sub(r"\b[a-zA-Z]\w*\s*=\s*", "", s)

    s = s.replace("±", "+-").replace("\\pm", "+-")
    # Expande +-X ou +- X em X, -X
    s = re.sub(r"\+\s*-\s*([^\s,;\}]+)", r"\1, -\1", s)
    s = re.sub(r"(?<![a-zA-Z0-9)])-\s*\+\s*([^\s,;\}]+)", r"\1, -\1", s)
    # Remove delimitadores externos { } ou ( ) ou [ ]
    s_limpo = re.sub(r"\b(?:ou|e|and|or)\b", ",", s, flags=re.IGNORECASE)
    s_limpo = s_limpo.strip().lstrip("{").rstrip("}").lstrip("[").rstrip("]")
    if s_limpo.startswith("(") and s_limpo.endswith(")"):
        s_limpo = s_limpo[1:-1]

    # Se houver virgula separando itens (com espaco ou fora de digitos decimais BR)
    # Normaliza virgulas decimais primeiro? No caso de conjunto, separamos por ';', ',', ou '\n'
    partes = _separar_nivel_zero(re.sub(r"(?<=\d),(?=\d)", lambda m: m.group(0), s_limpo), ",;\n")
    # Se o aluno escreveu decimal com virgula tipo "1,5; 2,5", ';' separa; se escreveu "1, 2", ',' separa.
    if ";" in s_limpo:
        partes = _separar_nivel_zero(s_limpo, ";\n")
    elif "," in s_limpo:
        # Separa apenas virgulas seguidas de espaco ou apos caractere nao digito ou antes de sinal/digito quando nao ha ';'
        partes = _separar_nivel_zero(s_limpo, ",\n")
    else:
        partes = _separar_nivel_zero(s_limpo, " \t\n")

    if not partes:
        raise ValueError("Nenhum numero encontrado no conjunto.")
    return [avaliar_escalar(p) for p in partes]


def _extrair_tuplas_balanceadas(texto: str) -> List[str]:
    """Extrai substrings top-level delimitadas por (...) ou [...]."""
    res: List[str] = []
    i = 0
    n = len(texto)
    while i < n:
        ch = texto[i]
        if ch in "([":
            ab = ch
            fc = ")" if ch == "(" else "]"
            depth = 1
            j = i + 1
            while j < n and depth > 0:
                if texto[j] == ab:
                    depth += 1
                elif texto[j] == fc:
                    depth -= 1
                j += 1
            if depth == 0:
                res.append(texto[i:j])
                i = j
                continue
        i += 1
    return res


def _parse_vetor(texto: Any) -> List[Tuple[Optional[Fraction], float]]:
    if isinstance(texto, list):
        return [avaliar_escalar(x) for x in texto]

    s = str(texto or "").strip()
    if "=" in s and not any(k in s for k in ["(", "["]):
        s = s.split("=")[-1].strip()
    elif "=" in s:
        # Ex: v = (1, 2, 3) ou n = (2, -1, 3)
        lhs, rhs = s.split("=", 1)
        if any(ch in rhs for ch in ("(", "[", "i", "j", "k")):
            s = rhs.strip()

    # Tenta forma (x, y, z) ou [x, y, z] mesmo com chamadas sqrt(...) internas
    tuplas = _extrair_tuplas_balanceadas(s)
    if tuplas and not re.search(r"\\hat|\\vec|\b[ijk]\b|\\imath|\\jmath", s):
        interno = tuplas[0][1:-1].strip()
        if ";" in interno:
            coords = _separar_nivel_zero(interno, ";")
        else:
            coords = _separar_nivel_zero(interno, ",")
            if len(coords) == 1:
                coords = re.split(r"\s+", interno)
        return [avaliar_escalar(c) for c in coords if c.strip()]

    # Forma canonica ai + bj + ck (ou \hat{\imath}, etc.)
    s_can = _converter_latex_basico(s)
    s_can = s_can.replace("\\hat(i)", "i").replace("\\hat(j)", "j").replace("\\hat(k)", "k")
    s_can = re.sub(r"hat\((?:\\?i|imath)\)|\\imath", "i", s_can)
    s_can = re.sub(r"hat\((?:\\?j|jmath)\)|\\jmath", "j", s_can)
    s_can = re.sub(r"hat\((?:\\?k)\)", "k", s_can)
    if re.search(r"\b[ijk]\b", s_can):
        # Troca i->0, j->0, k->0 via variaveis em _eval_ast_node
        def _aval_ijk(expr_str: str, vi: float, vj: float, vk: float) -> float:
            norm = _normalizar_expr_python(expr_str)
            tree = ast.parse(norm, mode="eval")
            return float(_eval_ast_node(tree, {"i": vi, "j": vj, "k": vk}, False))

        # Extrair expressao limpa (caso tenha "v = ...")
        expr_clean = s_can.split("=")[-1].strip() if "=" in s_can else s_can
        c_i = _aval_ijk(expr_clean, 1.0, 0.0, 0.0)
        c_j = _aval_ijk(expr_clean, 0.0, 1.0, 0.0)
        c_k = _aval_ijk(expr_clean, 0.0, 0.0, 1.0)
        # Se k nao aparece e nao foi citado, decide 2D vs 3D se necessario na comparacao
        if "k" in expr_clean:
            return [(Fraction(c_i).limit_denominator(10**6), c_i),
                    (Fraction(c_j).limit_denominator(10**6), c_j),
                    (Fraction(c_k).limit_denominator(10**6), c_k)]
        return [(None, c_i), (None, c_j)]

    # Fallback: separado por virgula ou ponto-e-virgula ou espacos
    interno = s.strip("()[] ")
    if ";" in interno:
        coords = _separar_nivel_zero(interno, ";")
    elif "," in interno:
        coords = _separar_nivel_zero(interno, ",")
    else:
        coords = re.split(r"\s+", interno)
    return [avaliar_escalar(c) for c in coords if c.strip()]


def _parse_matriz(texto: Any) -> List[List[Tuple[Optional[Fraction], float]]]:
    if isinstance(texto, list):
        return [[avaliar_escalar(cel) for cel in linha] for linha in texto]

    s = str(texto or "").strip()
    # Remover lado esquerdo "A =", "X =", "(AB)^T ="
    if "=" in s:
        lhs, rhs = s.split("=", 1)
        if "[" in rhs or "\\begin" in rhs:
            s = rhs.strip()

    # Formato LaTeX \begin{bmatrix} ... \end{bmatrix} ou pmatrix
    m_tex = re.search(r"\\begin\{[bpvV]?matrix\}(.*?)\\end\{[bpvV]?matrix\}", s, re.DOTALL)
    if m_tex:
        corpo = m_tex.group(1).strip()
        linhas_raw = re.split(r"\\\\|\n", corpo)
        mat = []
        for ln in linhas_raw:
            ln = ln.strip()
            if not ln:
                continue
            cols = [c.strip() for c in ln.split("&") if c.strip()]
            mat.append([avaliar_escalar(c) for c in cols])
        if mat:
            return mat

    # Formato Python / JSON: [[1, 2], [3, 4]]
    s_clean = re.sub(r"\s+", " ", s).strip()
    if s_clean.startswith("[") and "[" in s_clean[1:]:
        # Extrair sub-listas entre [...]
        inner = s_clean[1:-1].strip()
        linhas_str = re.findall(r"\[([^\[\]]+)\]", inner)
        if linhas_str:
            mat = []
            for ls in linhas_str:
                if ";" in ls:
                    cols = _separar_nivel_zero(ls, ";")
                elif "," in ls:
                    cols = _separar_nivel_zero(ls, ",")
                else:
                    cols = re.split(r"\s+", ls.strip())
                mat.append([avaliar_escalar(c) for c in cols if c.strip()])
            return mat

    # Formato MATLAB: [1 2; 3 4] ou [1, 2; 3, 4]
    if ";" in s_clean:
        inner = s_clean.strip("[] ")
        linhas_raw = [x.strip() for x in inner.split(";") if x.strip()]
        mat = []
        for ln in linhas_raw:
            cols = _separar_nivel_zero(ln, ",") if "," in ln else re.split(r"\s+", ln)
            mat.append([avaliar_escalar(c) for c in cols if c.strip()])
        if mat:
            return mat

    # Formato multi-linha textual (com ou sem colchetes por linha)
    linhas_txt = [ln.strip("[]| \t") for ln in str(texto).splitlines() if ln.strip("[]| \t")]
    if linhas_txt:
        mat = []
        for ln in linhas_txt:
            cols = _separar_nivel_zero(ln, ",") if "," in ln else re.split(r"\s+", ln)
            if cols:
                mat.append([avaliar_escalar(c) for c in cols if c.strip()])
        if mat:
            return mat

    raise ValueError("Nao foi possivel interpretar a matriz submetida.")


def _vetores_iguais(
    v1: List[Tuple[Optional[Fraction], float]],
    v2: List[Tuple[Optional[Fraction], float]],
    tol: float = 1e-3,
    aceitar_multiplo: bool = False,
    aceitar_oposto: bool = False,
) -> bool:
    if len(v1) != len(v2):
        # Caso vetor 2D escrito com i, j comparado com 3D terminado em 0
        if len(v1) == 2 and len(v2) == 3 and abs(v2[2][1]) <= tol:
            v1 = v1 + [(Fraction(0), 0.0)]
        else:
            return False

    def _comp_elem(a: Tuple[Optional[Fraction], float], b: Tuple[Optional[Fraction], float]) -> bool:
        if a[0] is not None and b[0] is not None:
            return a[0] == b[0]
        return abs(a[1] - b[1]) <= tol * max(1.0, abs(b[1]))

    if all(_comp_elem(a, b) for a, b in zip(v1, v2)):
        return True

    if aceitar_oposto:
        v1_op = [((-a[0] if a[0] is not None else None), -a[1]) for a in v1]
        if all(_comp_elem(a, b) for a, b in zip(v1_op, v2)):
            return True

    if aceitar_multiplo:
        n1 = math.sqrt(sum(a[1] ** 2 for a in v1))
        n2 = math.sqrt(sum(b[1] ** 2 for b in v2))
        if n1 <= 1e-9 or n2 <= 1e-9:
            return False
        # Verifica colinearidade: u x v == 0 (para 2D/3D) ou razao constante
        if len(v1) == 3:
            cross = [
                v1[1][1] * v2[2][1] - v1[2][1] * v2[1][1],
                v1[2][1] * v2[0][1] - v1[0][1] * v2[2][1],
                v1[0][1] * v2[1][1] - v1[1][1] * v2[0][1],
            ]
            return math.sqrt(sum(c ** 2 for c in cross)) <= tol * max(1.0, n1 * n2)
        ratios = [a[1] / b[1] for a, b in zip(v1, v2) if abs(b[1]) > 1e-9]
        if any(abs(b[1]) <= 1e-9 and abs(a[1]) > tol for a, b in zip(v1, v2)):
            return False
        if not ratios:
            return False
        k = ratios[0]
        return all(abs(r - k) <= tol * max(1.0, abs(k)) for r in ratios)

    return False


def _avaliar_expr_com_vars(expr_str: str, vars_dict: Dict[str, float]) -> float:
    norm = _normalizar_expr_python(expr_str)
    tree = ast.parse(norm, mode="eval")
    vmap = {k.lower(): float(v) for k, v in vars_dict.items()}
    return float(_eval_ast_node(tree, vmap, False))


def _extrair_lhs_menos_rhs(equacao: str) -> str:
    s = str(equacao or "").strip()
    # Remove prefixo de rotulo "pi:", "r:", "c:" antes de equacao
    s = re.sub(r"^(?:pi|π|plano|reta|eq\.?|equacao)\s*:\s*", "", s, flags=re.IGNORECASE).strip()
    if "=" not in s:
        return s
    lhs, rhs = s.split("=", 1)
    return f"({lhs.strip()}) - ({rhs.strip()})"


def _avaliar_plano(resp: str, esperado_abcd: List[Any], tol: float) -> Tuple[bool, str]:
    coeffs_ref = [avaliar_escalar(x)[1] for x in esperado_abcd]
    if len(coeffs_ref) != 4:
        return False, "Especificacao de plano invalida."
    norm_ref = math.sqrt(sum(c * c for c in coeffs_ref[:3]))
    if norm_ref <= 1e-9:
        return False, "Vetor normal de referencia nulo."

    try:
        expr = _extrair_lhs_menos_rhs(resp)
        d0 = _avaliar_expr_com_vars(expr, {"x": 0.0, "y": 0.0, "z": 0.0})
        a_alu = _avaliar_expr_com_vars(expr, {"x": 1.0, "y": 0.0, "z": 0.0}) - d0
        b_alu = _avaliar_expr_com_vars(expr, {"x": 0.0, "y": 1.0, "z": 0.0}) - d0
        c_alu = _avaliar_expr_com_vars(expr, {"x": 0.0, "y": 0.0, "z": 1.0}) - d0
    except Exception as exc:
        return False, f"Nao foi possivel ler a equacao geral do plano ({exc})."

    # Conferir linearidade em um ponto extra (1,2,3)
    esperado_lin = a_alu * 1.0 + b_alu * 2.0 + c_alu * 3.0 + d0
    real_pt = _avaliar_expr_com_vars(expr, {"x": 1.0, "y": 2.0, "z": 3.0})
    if abs(real_pt - esperado_lin) > tol * 10:
        return False, "A equacao submetida nao e linear em x, y, z."

    norm_alu = math.sqrt(a_alu ** 2 + b_alu ** 2 + c_alu ** 2)
    if norm_alu <= 1e-9:
        return False, "Vetor normal da equacao do plano esta nulo."

    # Normaliza ambos para comparar proporcionalidade [a,b,c,d]
    vec_alu = [a_alu / norm_alu, b_alu / norm_alu, c_alu / norm_alu, d0 / norm_alu]
    vec_ref = [c / norm_ref for c in coeffs_ref]

    ok_pos = all(abs(x - y) <= tol for x, y in zip(vec_alu, vec_ref))
    ok_neg = all(abs(x + y) <= tol for x, y in zip(vec_alu, vec_ref))
    if ok_pos or ok_neg:
        return True, "Equacao do plano equivalente ao gabarito."
    return False, "Os coeficientes ou termo independente do plano divergem do gabarito."


def _parse_reta_geometria(resp: str, tol: float) -> Tuple[List[float], List[float]]:
    """
    Extrai (ponto_P0, vetor_diretor_v) de qualquer representacao da reta em R^3:
    1) Vetorial: (x,y,z) = (x0,y0,z0) + t(a,b,c)
    2) Parametrica: x = x0 + at, y = y0 + bt, z = z0 + ct
    3) Reduzida (com ou sem coordenada constante): y = mx + n, z = px + q (ou x = c1, z = c2, etc.)
    4) Simetrica: (x - x0)/a = (y - y0)/b = (z - z0)/c (incluindo parte fixa "; x = 1")
    """
    s = str(resp or "").strip()
    s = re.sub(r"^(?:r|s|r1|r2|reta)\s*:\s*", "", s, flags=re.IGNORECASE).strip()
    s = s.replace("{", "").replace("}", "")

    # 1) Vetorial: (x,y,z) = (x0,y0,z0) + t*(a,b,c)
    m_vet = re.search(
        r"\(([^()]+)\)\s*\+\s*[thsp]\s*\*?\s*\(([^()]+)\)",
        s,
        re.IGNORECASE,
    )
    if m_vet:
        p0 = [avaliar_escalar(x)[1] for x in _separar_nivel_zero(m_vet.group(1), ",")]
        v0 = [avaliar_escalar(x)[1] for x in _separar_nivel_zero(m_vet.group(2), ",")]
        if len(p0) == 3 and len(v0) == 3:
            return p0, v0

    # Separar clausulas por ',' (fora de parenteses), ';' ou quebra de linha
    clausulas = [c.strip() for c in _separar_nivel_zero(s, ";\n,") if c.strip()]
    # Recombinar se algum ponto teve ',' dentro (ja tratado por nivel_zero)

    # 2) Parametrica (detecta parametro t, h, s ou p em equacoes de x=, y=, z=)
    # Normaliza cada clausula buscando atribuicao direta a x, y, z
    eq_map: Dict[str, str] = {}
    simetricas: List[str] = []
    for cl in clausulas:
        m_var = re.match(r"^([xyz])\s*=\s*(.+)$", cl, re.IGNORECASE)
        if m_var and "=" not in m_var.group(2):
            eq_map[m_var.group(1).lower()] = m_var.group(2).strip()
        elif "=" in cl:
            simetricas.append(cl)

    # Verificar se eh parametrica em t (ou h, s)
    if len(eq_map) == 3 and any(re.search(r"\b[ths]\b", v, re.IGNORECASE) for v in eq_map.values()):
        param = "t"
        for cand in ("t", "h", "s"):
            if any(re.search(rf"\b{cand}\b", v, re.IGNORECASE) for v in eq_map.values()):
                param = cand
                break
        p0, v0 = [], []
        for eixo in ("x", "y", "z"):
            ex = eq_map[eixo]
            c0 = _avaliar_expr_com_vars(ex, {param: 0.0})
            c1 = _avaliar_expr_com_vars(ex, {param: 1.0})
            p0.append(c0)
            v0.append(c1 - c0)
        return p0, v0

    # 3) Reduzida em x, y ou z, ou duas coordenadas constantes
    if len(eq_map) >= 2 and not simetricas:
        vars_faltando = [e for e in ("x", "y", "z") if e not in eq_map]
        if len(vars_faltando) == 1:
            indep = vars_faltando[0]
            # Avaliar em indep=0 e indep=1
            p0_d = {indep: 0.0}
            p1_d = {indep: 1.0}
            for e, ex in eq_map.items():
                p0_d[e] = _avaliar_expr_com_vars(ex, {indep: 0.0})
                p1_d[e] = _avaliar_expr_com_vars(ex, {indep: 1.0})
            p0 = [p0_d["x"], p0_d["y"], p0_d["z"]]
            v0 = [p1_d["x"] - p0_d["x"], p1_d["y"] - p0_d["y"], p1_d["z"] - p0_d["z"]]
            return p0, v0

    # 4) Simetrica (possivelmente combinada com 1 coordenada constante em eq_map)
    if simetricas:
        partes_eq = []
        for seg in simetricas:
            partes_eq.extend([p.strip() for p in seg.split("=") if p.strip()])
        # Encontrar expressao para t = parte_eq[0], onde uma das variaveis aparece em cada parte
        # Abordagem geral: parametrizamos encontrando dois pontos P(0) e P(1) que satisfacam todas as equacoes!
        # Cada parte com variavel e linear: A_k * var + B_k = lam
        coef_por_var: Dict[str, Tuple[float, float]] = {}
        for p_txt in partes_eq:
            vars_p = [v for v in ("x", "y", "z") if re.search(rf"\b{v}\b", p_txt, re.IGNORECASE)]
            if len(vars_p) == 1:
                vr = vars_p[0]
                b_v = _avaliar_expr_com_vars(p_txt, {vr: 0.0})
                a_v = _avaliar_expr_com_vars(p_txt, {vr: 1.0}) - b_v
                coef_por_var[vr] = (a_v, b_v)
        for vr, ex in eq_map.items():
            # Coordenada constante vr = const (ex.: x = 3)
            val_const = _avaliar_expr_com_vars(ex, {"x": 0.0, "y": 0.0, "z": 0.0})
            coef_por_var[vr] = (float("inf"), val_const)

        if len(coef_por_var) == 3:
            p0, v0 = [], []
            for vr in ("x", "y", "z"):
                a_v, b_v = coef_por_var[vr]
                if math.isinf(a_v):
                    p0.append(b_v)
                    v0.append(0.0)
                else:
                    if abs(a_v) <= 1e-12:
                        raise ValueError("Denominador ou coeficiente nulo na forma simetrica.")
                    # a_v * coord + b_v = lam => coord(0) = -b_v/a_v, dir = 1/a_v
                    p0.append(-b_v / a_v)
                    v0.append(1.0 / a_v)
            return p0, v0

    raise ValueError("Formato de reta nao reconhecido (use vetorial, parametrica, simetrica ou reduzida).")


def _avaliar_reta(resp: str, spec_reta: Dict[str, Any], tol: float) -> Tuple[bool, str]:
    p_ref = [avaliar_escalar(x)[1] for x in spec_reta["ponto"]]
    v_ref = [avaliar_escalar(x)[1] for x in spec_reta["diretor"]]
    norm_ref = math.sqrt(sum(c * c for c in v_ref))
    if norm_ref <= 1e-9:
        return False, "Vetor diretor de referencia nulo."

    try:
        p_alu, v_alu = _parse_reta_geometria(resp, tol)
    except Exception as exc:
        return False, f"Nao foi possivel interpretar a reta: {exc}"

    norm_alu = math.sqrt(sum(c * c for c in v_alu))
    if norm_alu <= 1e-9:
        return False, "Vetor diretor obtido e nulo."

    # 1. Vetores diretores devem ser paralelos: v_alu x v_ref == 0
    cross_v = [
        v_alu[1] * v_ref[2] - v_alu[2] * v_ref[1],
        v_alu[2] * v_ref[0] - v_alu[0] * v_ref[2],
        v_alu[0] * v_ref[1] - v_alu[1] * v_ref[0],
    ]
    if math.sqrt(sum(c * c for c in cross_v)) > tol * max(1.0, norm_alu * norm_ref):
        return False, "A direcao (vetor diretor) da reta nao coincide com o gabarito."

    # 2. Ponto P_alu deve pertencer a reta de referencia: (P_alu - P_ref) x v_ref == 0
    diff_p = [p_alu[0] - p_ref[0], p_alu[1] - p_ref[1], p_alu[2] - p_ref[2]]
    cross_p = [
        diff_p[1] * v_ref[2] - diff_p[2] * v_ref[1],
        diff_p[2] * v_ref[0] - diff_p[0] * v_ref[2],
        diff_p[0] * v_ref[1] - diff_p[1] * v_ref[0],
    ]
    norm_dp = math.sqrt(sum(c * c for c in diff_p))
    if math.sqrt(sum(c * c for c in cross_p)) > tol * max(1.0, norm_dp * norm_ref):
        return False, "O ponto escolhido da equacao nao pertence a reta esperada."

    return True, "Equacao da reta geometricamente equivalente ao gabarito."


def _avaliar_equacao_algebrica(resp: str, spec_eq: Dict[str, Any], tol: float) -> Tuple[bool, str]:
    variaveis = [str(v).lower() for v in spec_eq.get("variaveis", ["x", "y"])]
    expr_ref = str(spec_eq.get("expr", ""))
    pontos_teste = spec_eq.get("pontos_teste", [])
    if not pontos_teste:
        return False, "Especificacao de equacao sem pontos de teste."

    try:
        expr_alu = _extrair_lhs_menos_rhs(resp)
        # Rejeita identidade trivial 0 = 0 verificando ao menos 2 pontos deslocados fora da curva
        vals_on = []
        for pt in pontos_teste:
            vmap = {var: avaliar_escalar(val)[1] for var, val in zip(variaveis, pt)}
            v_alu = _avaliar_expr_com_vars(expr_alu, vmap)
            vals_on.append(abs(v_alu))

        if max(vals_on) > tol * 5:
            return False, "A equacao informada nao e satisfeita pelos pontos da curva/condicao esperada."

        # Verificar que a equacao nao e identicamente zero em pontos fora do lugar geometrico
        nao_nulos = 0
        for shift in (1.73, -2.41, 3.19):
            base_pt = {var: avaliar_escalar(val)[1] + shift for var, val in zip(variaveis, pontos_teste[0])}
            v_ref_out = abs(_avaliar_expr_com_vars(expr_ref, base_pt))
            v_alu_out = abs(_avaliar_expr_com_vars(expr_alu, base_pt))
            if v_ref_out > tol * 10 and v_alu_out > tol * 10:
                nao_nulos += 1

        if nao_nulos == 0:
            return False, "Expressao trivial ou degenerada (anula pontos que nao satisfazem a equacao)."

        return True, "Equacao algebrica equivalente ao gabarito."
    except Exception as exc:
        return False, f"Nao foi possivel validar a equacao ({exc})."


def _normalizar_rotulo(txt: str) -> str:
    s = remover_acentos(txt).lower().strip()
    s = re.sub(r"[-_]+", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s


def _avaliar_classificacao(resp: str, spec: Dict[str, Any]) -> Tuple[bool, str]:
    resp_norm = _normalizar_rotulo(resp)
    esperado = _normalizar_rotulo(str(spec.get("esperado", "")))
    sinonimos = [_normalizar_rotulo(x) for x in spec.get("sinonimos", [])]
    candidatos = [c for c in [esperado] + sinonimos if c]

    for cand in candidatos:
        if resp_norm == cand:
            return True, f"Classificacao correta ('{spec.get('esperado')}')."
        if re.search(rf"(?<![a-z0-9]){re.escape(cand)}(?![a-z0-9])", resp_norm):
            # Evitar falso positivo se houver negacao explicita imediata antes
            m = re.search(rf"(?<![a-z0-9]){re.escape(cand)}(?![a-z0-9])", resp_norm)
            prefix = resp_norm[max(0, m.start() - 15):m.start()]
            if not re.search(r"\bnao\b|\bsem\b|\bincorret", prefix):
                return True, f"Classificacao correta ('{spec.get('esperado')}')."

    return False, f"Classificacao esperada: '{spec.get('esperado')}'."


def _extrair_subitens_resposta(resp: str, chaves: List[str]) -> Dict[str, str]:
    """Extrai secoes etiquetadas (a)/(b), a:/b:, foco:/diretriz: ou linhas correspondentes."""
    achados: Dict[str, str] = {}
    s = str(resp or "").strip()

    # Monta regex combinando todas as chaves possiveis
    # Ex: "(a) ... (b) ..." ou "foco: ... diretriz: ..." ou "a) ... b) ..."
    pad_parts = []
    for k in chaves:
        ek = re.escape(k)
        if len(k) == 1:
            pad_parts.append(rf"(?:\(\s*{ek}\s*\)|\b{ek}\s*[\)\:\-])")
        else:
            pad_parts.append(rf"(?:\b{ek}\s*[\:\-])")

    pad = re.compile(r"(" + "|".join(pad_parts) + r")", re.IGNORECASE)
    matches = list(pad.finditer(s))
    if matches:
        for idx, m in enumerate(matches):
            rot_raw = re.sub(r"[^a-zA-Z0-9_]", "", remover_acentos(m.group(1)).lower())
            # Normaliza para a chave correspondente
            chave_norm = rot_raw
            for k in chaves:
                if remover_acentos(k).lower() == rot_raw:
                    chave_norm = k
                    break
            ini = m.end()
            fim = matches[idx + 1].start() if idx + 1 < len(matches) else len(s)
            achados[chave_norm] = s[ini:fim].strip(" ;|\n")
        if len(achados) >= len(chaves):
            return achados

    # Fallback: se nao usou rotulos mas escreveu exatamente N segmentos separados por ';' ou '|' ou linha
    linhas = [ln.strip() for ln in _separar_nivel_zero(s, ";|\n") if ln.strip()]
    if len(linhas) == len(chaves):
        for k, ln in zip(chaves, linhas):
            achados[k] = ln
        return achados

    return achados


def avaliar_resposta_matematica(
    resposta_aluno: str,
    spec: Dict[str, Any],
    questao_id: str,
    tol: float = 1e-3,
) -> Tuple[bool, str, str, float]:
    """
    Avalia resposta matematica usando Python exato (Fraction + AST + geometria analitica).
    Retorna: (ok, categoria_erro, feedback_detalhado, confianca).
    """
    resp = str(resposta_aluno or "").strip()
    if not resp:
        return (
            False,
            "resposta_em_branco",
            f"[{questao_id}] Questao em branco ou ilegivel na imagem.",
            1.0,
        )

    tipo = str(spec.get("tipo_resposta", "numero")).strip().lower()
    dica_erro = str(spec.get("dica_erro", "")).strip()

    try:
        if tipo == "numero":
            ok = _iguais_escalar(resp, spec["esperado"], tol=tol)
            if ok:
                return True, "sem_erro", f"[{questao_id}] Valor exato conferido pelo oraculo matematico.", 0.99
            return (
                False,
                "erro_calculo_ou_sinal",
                f"[{questao_id}] Valor numerico diverge do esperado. {dica_erro}".strip(),
                0.98,
            )

        if tipo == "conjunto_numeros":
            obt = _parse_conjunto_numeros(resp)
            esp = _parse_conjunto_numeros(spec["esperado"])
            if len(obt) != len(esp):
                return (
                    False,
                    "raiz_ou_solucao_faltante",
                    f"[{questao_id}] Quantidade de valores difere do esperado (atencao a sinais +- e raizes multiplas). {dica_erro}".strip(),
                    0.97,
                )
            usados = set()
            for item_e in esp:
                achou = False
                for idx_o, item_o in enumerate(obt):
                    if idx_o in usados:
                        continue
                    if _iguais_escalar(
                        item_o[0] if item_o[0] is not None else item_o[1],
                        item_e[0] if item_e[0] is not None else item_e[1],
                        tol=tol,
                    ):
                        usados.add(idx_o)
                        achou = True
                        break
                if not achou:
                    return (
                        False,
                        "erro_calculo_ou_sinal",
                        f"[{questao_id}] Um ou mais valores do conjunto divergem do esperado. {dica_erro}".strip(),
                        0.97,
                    )
            return True, "sem_erro", f"[{questao_id}] Conjunto completo de valores conferido com exatidao.", 0.99

        if tipo == "matriz":
            m_obt = _parse_matriz(resp)
            m_esp = _parse_matriz(spec["esperado"])
            if len(m_obt) != len(m_esp) or any(len(r1) != len(r2) for r1, r2 in zip(m_obt, m_esp)):
                return (
                    False,
                    "ordem_matriz_incorreta",
                    f"[{questao_id}] Dimensoes da matriz submetida divergem da ordem esperada ({len(m_esp)}x{len(m_esp[0])}). {dica_erro}".strip(),
                    0.99,
                )
            for i, (r_o, r_e) in enumerate(zip(m_obt, m_esp)):
                for j, (c_o, c_e) in enumerate(zip(r_o, r_e)):
                    vo = c_o[0] if c_o[0] is not None else c_o[1]
                    ve = c_e[0] if c_e[0] is not None else c_e[1]
                    if not _iguais_escalar(vo, ve, tol=tol):
                        return (
                            False,
                            "elemento_matriz_incorreto",
                            f"[{questao_id}] Elemento na posicao ({i+1},{j+1}) diverge do gabarito. {dica_erro}".strip(),
                            0.99,
                        )
            return True, "sem_erro", f"[{questao_id}] Todos os elementos da matriz conferem exatamente.", 0.99

        if tipo == "vetor":
            v_obt = _parse_vetor(resp)
            v_esp = _parse_vetor(spec["esperado"])
            ok = _vetores_iguais(
                v_obt,
                v_esp,
                tol=tol,
                aceitar_multiplo=bool(spec.get("aceitar_multiplo_nao_nulo", False)),
                aceitar_oposto=bool(spec.get("aceitar_oposto", False)),
            )
            if ok:
                return True, "sem_erro", f"[{questao_id}] Vetor/coordenadas conferem exatamente com o gabarito.", 0.99
            return (
                False,
                "vetor_ou_coordenada_incorreta",
                f"[{questao_id}] Componentes do vetor divergem do esperado. {dica_erro}".strip(),
                0.98,
            )

        if tipo == "conjunto_vetores":
            # Parse cada vetor encontrado (...) ou [...] (mesmo com sqrt(...) interno)
            s_cv = resp.strip()
            if s_cv.startswith("[") and s_cv.endswith("]") and "(" in s_cv[1:-1]:
                s_cv = s_cv[1:-1]
            blocos_v = _extrair_tuplas_balanceadas(s_cv)
            if not blocos_v:
                blocos_v = [ln.strip() for ln in _separar_nivel_zero(s_cv, ";\n") if ln.strip()]
            v_obts = [_parse_vetor(b) for b in blocos_v]
            v_esps = [_parse_vetor(x) for x in spec["esperado"]]
            if len(v_obts) != len(v_esps):
                return (
                    False,
                    "solucao_faltante",
                    f"[{questao_id}] Esperado(s) {len(v_esps)} vetor(es)/ponto(s), mas foram identificados {len(v_obts)}. {dica_erro}".strip(),
                    0.97,
                )
            usados = set()
            for ve in v_esps:
                achou = False
                for idx_o, vo in enumerate(v_obts):
                    if idx_o in usados:
                        continue
                    if _vetores_iguais(vo, ve, tol=tol):
                        usados.add(idx_o)
                        achou = True
                        break
                if not achou:
                    return (
                        False,
                        "vetor_ou_coordenada_incorreta",
                        f"[{questao_id}] Pelo menos um vetor/ponto diverge do esperado. {dica_erro}".strip(),
                        0.97,
                    )
            return True, "sem_erro", f"[{questao_id}] Todos os vetores/pontos esperados conferem.", 0.99

        if tipo == "plano":
            ok, msg = _avaliar_plano(resp, spec["esperado"], tol=tol)
            if ok:
                return True, "sem_erro", f"[{questao_id}] {msg}", 0.99
            return False, "equacao_plano_incorreta", f"[{questao_id}] {msg} {dica_erro}".strip(), 0.97

        if tipo == "reta":
            ok, msg = _avaliar_reta(resp, spec["esperado"], tol=tol)
            if ok:
                return True, "sem_erro", f"[{questao_id}] {msg}", 0.98
            return False, "equacao_reta_incorreta", f"[{questao_id}] {msg} {dica_erro}".strip(), 0.96

        if tipo == "equacao_algebrica":
            ok, msg = _avaliar_equacao_algebrica(resp, spec["esperado"], tol=tol)
            if ok:
                return True, "sem_erro", f"[{questao_id}] {msg}", 0.98
            return False, "equacao_conica_ou_condicao_incorreta", f"[{questao_id}] {msg} {dica_erro}".strip(), 0.96

        if tipo == "classificacao":
            ok, msg = _avaliar_classificacao(resp, spec)
            if ok:
                return True, "sem_erro", f"[{questao_id}] {msg}", 0.98
            return False, "classificacao_incorreta", f"[{questao_id}] {msg} {dica_erro}".strip(), 0.96

        if tipo == "composta":
            sub_specs: Dict[str, Any] = spec.get("esperado", {})
            chaves = list(sub_specs.keys())
            sub_resps = _extrair_subitens_resposta(resp, chaves)
            if len(sub_resps) < len(chaves):
                falt = [k for k in chaves if k not in sub_resps]
                return (
                    False,
                    "resposta_incompleta",
                    f"[{questao_id}] Faltou identificar subitem(ns): {', '.join(falt)}. Identifique cada parte claramente (ex.: (a) ... (b) ...). {dica_erro}".strip(),
                    0.95,
                )
            fbs = []
            for k in chaves:
                sub_ok, sub_cat, sub_fb, _ = avaliar_resposta_matematica(
                    sub_resps[k], sub_specs[k], f"{questao_id}({k})", tol=tol
                )
                if not sub_ok:
                    return False, sub_cat, sub_fb, 0.97
                fbs.append(sub_fb)
            return True, "sem_erro", f"[{questao_id}] Todos os subitens ({', '.join(chaves)}) estao corretos.", 0.99

    except Exception as exc:
        return (
            False,
            "formato_matematico_nao_interpretado",
            f"[{questao_id}] Nao foi possivel interpretar a resposta matematica ({exc}). {dica_erro}".strip(),
            0.85,
        )

    return False, "tipo_resposta_desconhecido", f"[{questao_id}] Tipo '{tipo}' nao suportado.", 0.5


if __name__ == "__main__":
    # Auto-teste unitario cobrindo todos os 10 tipos de validacao matematica
    assert avaliar_resposta_matematica("16/sqrt(21)", {"tipo_resposta": "numero", "esperado": "16*sqrt(21)/21"}, "T-NUM")[0]
    assert avaliar_resposta_matematica("m = +-9", {"tipo_resposta": "conjunto_numeros", "esperado": ["-9", "9"]}, "T-CNUM")[0]
    assert not avaliar_resposta_matematica("m = 9", {"tipo_resposta": "conjunto_numeros", "esperado": ["-9", "9"]}, "T-CNUM-F")[0]
    assert avaliar_resposta_matematica("\\begin{bmatrix} 1/2 & -1 \\\\ 0 & 3/2 \\end{bmatrix}", {"tipo_resposta": "matriz", "esperado": [["1/2", "-1"], ["0", "3/2"]]}, "T-MAT")[0]
    assert avaliar_resposta_matematica("(4, -2, 6)", {"tipo_resposta": "vetor", "esperado": [2, -1, 3], "aceitar_multiplo_nao_nulo": True}, "T-VEC")[0]
    assert avaliar_resposta_matematica("[(1,4,7), (1,0,1)]", {"tipo_resposta": "conjunto_vetores", "esperado": [[1, 0, 1], [1, 4, 7]]}, "T-CVEC")[0]
    assert avaliar_resposta_matematica("6x - 3y + 6z = 18", {"tipo_resposta": "plano", "esperado": [2, -1, 2, -6]}, "T-PLN")[0]
    assert avaliar_resposta_matematica("x = 2 + 2t, y = 1 - t, z = -3 + t", {"tipo_resposta": "reta", "esperado": {"ponto": [4, 0, -2], "diretor": [-2, 1, -1]}}, "T-RET1")[0]
    assert avaliar_resposta_matematica("y = -1/2 x + 2; z = 1/2 x - 4", {"tipo_resposta": "reta", "esperado": {"ponto": [2, 1, -3], "diretor": [2, -1, 1]}}, "T-RET2")[0]
    assert avaliar_resposta_matematica("(y-1)^2/9 - (x-3)^2/4 = 1", {"tipo_resposta": "equacao_algebrica", "esperado": {"variaveis": ["x", "y"], "expr": "9*(x-3)^2 - 4*(y-1)^2 + 36", "pontos_teste": [[3, 4], [3, -2], [5, 1 + 3 * math.sqrt(2)], [1, 1 - 3 * math.sqrt(2)]]}}, "T-CON")[0]
    assert avaliar_resposta_matematica("Matriz Simétrica", {"tipo_resposta": "classificacao", "esperado": "simetrica", "sinonimos": ["simetrica"]}, "T-CLS")[0]
    assert avaliar_resposta_matematica("(a) -4 (b) (-2, 6, 5)", {"tipo_resposta": "composta", "esperado": {"a": {"tipo_resposta": "numero", "esperado": -4}, "b": {"tipo_resposta": "vetor", "esperado": [-2, 6, 5]}}}, "T-CMP")[0]
    assert avaliar_resposta_matematica("2\\hat{\\imath} - \\hat{\\jmath} + 3\\hat{k}", {"tipo_resposta": "vetor", "esperado": [2, -1, 3]}, "T-IJK")[0]
    assert avaliar_resposta_matematica("(1/2, sqrt(3)/2, -1)", {"tipo_resposta": "vetor", "esperado": ["1/2", "sqrt(3)/2", -1]}, "T-VSQRT")[0]
    assert not avaliar_resposta_matematica("0 = 0", {"tipo_resposta": "equacao_algebrica", "esperado": {"variaveis": ["x", "y"], "expr": "x^2 - y", "pontos_teste": [[0, 0], [2, 4]]}}, "T-DEGEN")[0]
    print("SELF-TEST ORACULO MATEMATICO: OK (15/15 assercoes passaram)")
