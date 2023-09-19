import math 
#gcd - 최대 공약수, lcm - 최소 공배수
def solution(numer1, denom1, numer2, denom2):
    # 분자는 X 자 형태로 곱하고 더해야 함
    boonja = numer1 * denom2 + numer2 * denom1
    boonmo = denom1 * denom2
    
    gcd_value = math.gcd(boonmo, boonja)
    # 구해진 최대 공약수를 이용해 나누면 됨
    answer = [boonja/gcd_value, boonmo/gcd_value]
    return answer