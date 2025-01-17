def estimate_alipay_loss(daily_transaction_amount, market_share, incident_duration_minutes, discount_rate):
    """
    估算在特定事件中造成的财务损失。

    参数：
    - daily_transaction_amount (float): 每日总交易金额（单位：元）。
    - market_share (float): 支付宝的市场份额，十进制表示（例如 0.5 表示 50%）。
    - incident_duration_minutes (int): 事件持续时间（单位：分钟）。
    - discount_rate (float): 事件期间适用的折扣率，十进制表示（例如 0.2 表示 20%）。

    返回值：
    - float: 估算的损失金额（单位：元）。
    """
    # 支付宝的每日交易总额
    alipay_daily_transaction = daily_transaction_amount * market_share

    # 事件发生时占全天的比例
    proportion_of_day = incident_duration_minutes / (24 * 60)

    # 事件期间的交易金额
    transaction_during_incident = alipay_daily_transaction * proportion_of_day

    # 因折扣导致的估算损失
    estimated_loss = transaction_during_incident * discount_rate

    return estimated_loss


# 根据场景输入值
industry_daily_transaction_amount = 1.25e12  # 单位：元
alipay_market_share = 0.625  # 支付宝市场份额
incident_duration = 5  # 单位：分钟
discount_rate = 0.2  # 折扣率为 20%

# 估算损失
loss = estimate_alipay_loss(
    daily_transaction_amount=industry_daily_transaction_amount,
    market_share=alipay_market_share,
    incident_duration_minutes=incident_duration,
    discount_rate=discount_rate
)

# 输出结果
print("=== 支付宝损失估算 ===")
print(f"事件期间估算损失: {loss / 1e8:.2f} 亿元")
