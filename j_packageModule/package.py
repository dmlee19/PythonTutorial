# import travel.thailand # import의 마지막은 패키지 또는 모듈 단위만 올 수 있다.
# import travel.thailand.ThailandPackage # Error: class, method는 from import로 가능
# tripTo = travel.thailand.ThailandPackage()
# tripTo.detail()

# from travel.thailand import ThailandPackage
# tripTo = ThailandPackage()
# tripTo.detail()

# from travel import vietnam
# tripTo = vietnam.VietnamPackage()
# tripTo.detail()

# __all__
from travel import *  # package에 모든 것을 가지고 온다는 의미
# 개발자가 패키지 내부의 공개 범위를 설정해야 함 (__init__.py)
tripTo = vietnam.VietnamPackage()   # 오류
tripTo.detail()  # __init__.py 에 __all__ = ["vietnam"] 추가 후 에러 없이 실행
tripTo = thailand.ThailandPackage()   # 오류 (vietnam만 추가했기 때문에 )
tripTo.detail()  # __init__.py: __all__ = ["vietnam", "thailand"] 수정

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
