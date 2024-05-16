#
# 帰る時に月齢絵文字をSlackに投稿して帰宅しましたのマークにしている
# 毎回検索するの面倒になったからコード化
#
from datetime import datetime, timezone, timedelta

def get_moon_emoji(moon_age:int):
    moon_emoji = ["new_moon","waxing_crescent_moon","first_quarter_moon","moon","full_moon","waning_gibbous_moon","last_quarter_moon","waning_crescent_moon"]
    # 月齢に対応する絵文字を返す
    # 0 or 30 は new moon(0)
    # 1-6 が waxing crescent moon(1)
    # 7-8 が first quarter moon(2)
    # 9-14 が moon(3)
    # 15 が full moon(3)
    # 16-21 が waning gibbous moon(5)
    # 22-23 が last quarter moon(6)
    # 24-29 が waning crescent moon(7)
    index = 0
    if moon_age >= 1 and moon_age <= 6:
        index = 1
    elif moon_age == 7 :
        index = 2
    elif moon_age >= 8 and moon_age <= 14:
        index = 3
    elif moon_age == 15:
        index = 4
    elif moon_age >= 16 and moon_age <= 21:
        index = 5
    elif moon_age == 22:
        index = 6
    elif moon_age >= 23 and moon_age <= 29:
        index = 7

    return moon_emoji[index]

def calculate_jst_moon_age(date_jst):
    # 平均朔望月（新月から新月までの平均日数）
    synodic_month = 29.53058867

    # 2000年1月6日 18:14 (UTC) を基準とした新月の時刻
    base_date = datetime(2000, 1, 6, 18, 14, 000000, tzinfo=timezone.utc)
    # 基準日からの経過日数を計算
    delta = date_jst - base_date
    days = delta.total_seconds() / 86400

    # 月齢を計算
    moon_age = days % synodic_month
    return moon_age
JST = timezone(timedelta(hours=+9), 'JST')
print(f":{get_moon_emoji( round(calculate_jst_moon_age(datetime.now(JST))))}:")
