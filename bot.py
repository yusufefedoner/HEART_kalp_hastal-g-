import discord
from discord.ext import commands
from model import train_model, predict_with_confidence, explain_prediction

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

model = train_model()

@bot.event
async def on_ready():
    print(f"Bot aktif: {bot.user}")

def validate_inputs(age, bp, chol, maxhr):
    if not (0 < age < 120):
        return "Yaş geçersiz."
    if not (50 <= bp <= 250):
        return "Tansiyon değeri geçersiz."
    if not (0 <= chol <= 700):
        return "Kolesterol değeri geçersiz."
    if not (50 <= maxhr <= 250):
        return "MaxHR değeri geçersiz."
    return None

@bot.command()
async def kalp(ctx, age:int, sex:int, cp:int, bp:int, chol:int,
               fbs:int, ecg:int, maxhr:int, angina:int,
               oldpeak:float, slope:int):

    error = validate_inputs(age, bp, chol, maxhr)
    if error:
        await ctx.send(f"❌ **Hatalı Giriş:** {error}")
        return

    patient = [[
        age, sex, cp, bp, chol,
        fbs, ecg, maxhr, angina,
        oldpeak, slope
    ]]

    prediction, confidence = predict_with_confidence(model, patient)
    explanations = explain_prediction(model)

    if prediction == 1:
        result = "⚠️ **Kalp hastalığı riski VAR**"
    else:
        result = "✅ **Kalp hastalığı riski YOK**"

    explain_text = ""
    for f, _ in explanations:
        explain_text += f"- {f}\n"

    message = f"""{result}
**Tahmin Güveni:** %{confidence}
**En Etkili Faktörler:**
{explain_text}

⚠️ Bu sonuç tıbbi teşhis değildir.
Bir doktora danışınız.
"""

    await ctx.send(message)
bot.run("TOKEN")
