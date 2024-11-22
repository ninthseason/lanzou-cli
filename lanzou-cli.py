from lanzou.api import LanZouCloud
import utils
from utils import eprint
import sys


class Error:
    NOCOOKIE = -2
    BADARG = -3


if len(sys.argv) != 2:
    eprint("Usage: python lanzou-cli.py <file>")
    exit(Error.BADARG)

file = sys.argv[1]

utils.init()
lzc = LanZouCloud()


cookie = utils.get_cookie()
if cookie is None:
    eprint("Can't get cookie from cookie.json. Exiting.")
    exit(Error.NOCOOKIE)

login_result = lzc.login_by_cookie(cookie)

if login_result != LanZouCloud.SUCCESS:
    eprint("Login failed.")
    exit(login_result)


upload_result, fid = utils.upload_file(lzc, file, silent=True)

if upload_result != lzc.SUCCESS:
    eprint("Upload failed. Exiting")
    exit(upload_result)

fid = fid[0]

print(" ".join(utils.extract_durl(lzc, fid)))
