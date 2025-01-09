import pathlib
import json
import sys
from lanzou.api import LanZouCloud

work_dir = pathlib.Path(__file__).parent


def init():
    # check cookie file
    cookie_path = work_dir.joinpath("cookie.json")
    if not cookie_path.exists():
        print("cookie.json doesn't exist. creating it.")
        cookie_path.touch()


def get_cookie():
    try:
        cookie_path = work_dir.joinpath("cookie.json")
        with cookie_path.open() as f:
            return json.load(f)
    except:
        return None


def upload_file(lzc: LanZouCloud, path, silent=True):
    fid = []

    def process_cb(fn, ts, ns):
        print(f"{fn}: {ns}/{ts}")

    def finish_cb(fid_, is_file):
        fid.append(fid_)

    upload_result = lzc.upload_file(
        path, callback=process_cb if not silent else None, uploaded_handler=finish_cb
    )
    return upload_result, fid


def extract_durl(lzc: LanZouCloud, fid):
    fd = lzc.get_file_info_by_id(fid)
    return [fd.url, fd.pwd, fd.durl]


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
