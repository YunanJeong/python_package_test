"""
직접적으로 실행되는 시작스크립트(main).

- 설치된 파이썬 패키지는 import해서 라이브러리로 사용가능하지만,
- 많은 패키지들은 직접실행할 수 있는 기능을 제공한다.
- 직접실행시 __main__.py 가 프로그램의 시작점이 된다.

- 여기서는 입력인자 3개(설정파일, 시간, 시간)를 받아 처리하는 예시를 사용했다.
    - 실행시 시간인자를 입력하지 않으면 디폴트로 현재시간이 할당되는 예제이다.

- 다음은 직접 실행방법의 예시이다. -m 옵션은 설치된 파이썬 패키지 경로를 참조할 떄 필요하다.
- $ python -m -r"parameter1" -s"parameter2" -e"parameter3"

"""
import argparse
import util
import datetime


def main(required, start, end):
    util.example_func(required)
    util.example_func_sub(start)
    util.example_func_sub(end)


if __name__ == '__main__':
    # 입력인자 처리
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--require", dest="required_param", action="store",
                        required=True)  # 실행에 반드시 필요한 인자임을 나타낸 옵션
    parser.add_argument("-s", "--start", dest="start_param", action="store")
    parser.add_argument("-e", "--end", dest="end_param", action="store")
    args = parser.parse_args()

    req = util.example_read_config(args.required_param)
    sta = datetime.now() if args.startdate is None else datetime.strptime(args.start_param, '%Y%m%d') # NOQA
    end = datetime.now() if args.enddate is None else datetime.strptime(args.end_param, '%Y%m%d') # NOQA

    # 실행
    main(req, sta, end)
