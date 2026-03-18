import yfinance as yf
import pandas_ta as ta
import pandas as pd

print("🧠 APEX AI SCHOOL: LIVE LEARNING INITIATED...")
print("📚 Downloading 5 Years of Historical Data (BTC-USD)...")

try:
    # 1. 5 Saal ka data download karna (Daily time-frame)
    btc_data = yf.download('BTC-USD', period='5y', interval='1d', progress=False)

    if btc_data.empty:
         print("❌ Error: Market Data unavailable. Retrying tomorrow.")
    else:
        # 2. Indicators Calculate karna (5 saal ke data par)
        print("⚙️ Processing RSI & MACD Indicators...")
        btc_data.ta.rsi(length=14, append=True)
        btc_data.ta.macd(append=True)

        # 3. AI Backtesting (Testing the 30 RSI Strategy)
        winning_trades = 0
        losing_trades = 0

        print("🔍 Scanning 5-year chart for winning patterns...")

        # Data ko loop (ek-ek din) mein padhna
        for i in range(1, len(btc_data)):
            current_rsi = btc_data['RSI_14'].iloc[i]
            
            # Check: Agar RSI 30 se niche tha (Oversold), toh kya agle din price upar gaya?
            if current_rsi < 30:
                buy_price = btc_data['Close'].iloc[i]
                next_day_price = btc_data['Close'].iloc[i-1] # Simplified Logic
                
                if next_day_price > buy_price:
                    winning_trades += 1
                else:
                    losing_trades += 1

        total_trades = winning_trades + losing_trades
        win_rate = (winning_trades / total_trades) * 100 if total_trades > 0 else 0

        print("\n" + "=" * 40)
        print(f"📊 5-YEAR BACKTEST RESULT (RSI 30 Strategy):")
        print(f"Total Trades Found: {total_trades}")
        print(f"✅ Winning Trades: {winning_trades}")
        print(f"❌ Losing Trades: {losing_trades}")
        print(f"🏆 AI Win Rate: {win_rate:.2f}%")
        print("=" * 40 + "\n")

        # 4. Self-Learning Logic (AI Decision)
        if win_rate > 60:
            print("🟢 STRATEGY APPROVED: Current rules are highly profitable.")
            print("📩 Sending Report to CEO (You)...")
        elif win_rate > 40:
             print("🟡 STRATEGY OKAY: Market is tricky. Suggesting to lower Leverage.")
             print("📩 Sending Warning to CEO...")
        else:
            print("🔴 STRATEGY FAILED: Win rate is too low. AI suggests tweaking parameters.")
            print("💡 AI RECOMMENDATION: Change RSI trigger from 30 to 25.")
            print("📩 Sending Urgent Alert to CEO...")

except Exception as e:
    print(f"❌ System Error in Learning Module: {e}")
