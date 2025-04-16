from datetime import datetime, timedelta
import time
import colorama
from colorama import Style


colorama.init(autoreset=True)

def rgb_to_ansi(r, g, b):
    """Convert RGB values to ANSI escape codes."""
    return f"\033[38;2;{r};{g};{b}m"

def gradient_text(text, start_color, end_color):
    """Applies a smooth color gradient to the text."""
    length = len(text)
    gradient = ""

    for i, char in enumerate(text):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * (i / length))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * (i / length))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * (i / length))
        gradient += rgb_to_ansi(r, g, b) + char

    return gradient + Style.RESET_ALL  

# Gradient from green (0, 255, 0) to blue (0, 0, 255)
start_rgb = (255, 0, 0)  # Green
end_rgb = (100, 100, 200)    # Blue
          #R    #G   #B

# Custom #########################################################################
def custom(letter, start_custom, end_custom):
    """Applies a smooth color gradient to the text."""
    longth = len(letter)
    degrade = ""

    for i, char in enumerate(text):
        r = int(start_custom[0] + (end_custom[0] - start_custom[0]) * (i / longth))
        g = int(start_custom[1] + (end_custom[1] - start_custom[1]) * (i / longth))
        b = int(start_custom[2] + (end_custom[2] - start_custom[2]) * (i / longth))
        degrade += rgb_to_ansi(r, g, b) + char

    return degrade + Style.RESET_ALL

start_custom = (0,0,0)
end_custom = (0,0,0)

#End of custom #####################################################################

        
repeat = True
now = datetime.now()

subject_list = """Accounting, Applications of Mathematics, Art and Design,🎨 
Biology, Business Management,📈
Chemistry, Computing Science,🖥️
Design and Manufacture, Drama,🎭
Economics, Engineering Science, English,📝
French,🥖
Geography, German, Graphic Communication, (no emoji for this :( )
History,👵
Italian,🍝
Latin,🍇
Mandarin, Maths, Music Performance, Music Tech,🎵
Physics,🧑‍🔬
MODS, ._.
Spanish, 👯 
"""

exam_dates = {
    "Accounting": datetime(2025, 5, 12, 13, 0),
    "Applications of Mathematics": datetime(2025, 5, 7, 9, 0),
    "Art and Design": "No written exam, coursework submission applies",
    "Biology": datetime(2025, 5, 6, 13, 0),
    "Business Management": datetime(2025, 5, 8, 13, 0),
    "Chemistry": datetime(2025, 5, 9, 9, 0),
    "Computing Science": datetime(2025, 4, 25, 9, 0),
    "Design and Manufacture": datetime(2025, 5, 5, 13, 0),
    "Drama": datetime(2025, 5, 14, 13, 0),
    "Economics": datetime(2025, 5, 13, 9, 0),
    "Engineering Science": datetime(2025, 5, 15, 9, 0),
    "English": datetime(2025, 4, 28, 9, 0),
    "French": datetime(2025, 5, 1, 9, 0),
    "Geography": datetime(2025, 4, 29, 13, 0),
    "German": datetime(2025, 5, 2, 9, 0),
    "Graphic Communication": datetime(2025, 4, 30, 13, 0),
    "History": datetime(2025, 5, 12, 9, 0),
    "Italian": datetime(2025, 5, 2, 13, 0),
    "Latin": datetime(2025, 5, 8, 9, 0),
    "Mandarin": datetime(2025, 5, 7, 13, 0),
    "Maths": datetime(2025, 5, 1, 13, 0),
    "Music Performance": "No written exam, practical assessment applies",
    "Music Technology": datetime(2025, 4, 28, 13, 0),
    "Physics": datetime(2025, 5, 14, 9, 0),
    "MODS": datetime(2025, 5, 9, 13, 0),
    "Spanish": datetime(2025, 5, 6, 9, 0)
}


print(gradient_text("""                           
                               ███╗   ██╗███████╗
                               ████╗  ██║██╔════╝
                               ██╔██╗ ██║███████╗
                               ██║╚██╗██║╚════██║
                               ██║ ╚████║███████║
                               ╚═╝  ╚═══╝╚══════╝
                  
                      ███████╗██╗  ██╗ █████╗ ███╗   ███╗                           
                      ██╔════╝╚██╗██╔╝██╔══██╗████╗ ████║                                               
                      █████╗   ╚███╔╝ ███████║██╔████╔██║                                               
                      ██╔══╝   ██╔██╗ ██╔══██║██║╚██╔╝██║                                               
                      ███████╗██╔╝ ██╗██║  ██║██║ ╚═╝ ██║                                               
                      ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝                                              
                                                                                 
 ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗
██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██║    ██║████╗  ██║
██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║   ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
██║     ██║   ██║██║   ██║██║╚██╗██║   ██║   ██║  ██║██║   ██║██║███╗██║██║╚██╗██║
╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║   ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║
 ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝

                                 made by Ohnoツ

                          https://github.com/OhnoMain
                          https://discord.gg/FgM4zAw4qP
                        
""", start_rgb, end_rgb))

time.sleep(2)
print(gradient_text("Welcome, please enter your desired subject from the list below (case sensitive)\n", start_rgb, end_rgb))
time.sleep(3)

while repeat:
    print(gradient_text(subject_list, start_rgb, end_rgb))
    time.sleep(2)
    choice = input(gradient_text(": ", start_rgb, end_rgb))
    if choice == "Time":
        print(now)
        choice = input(gradient_text(": ", start_rgb, end_rgb))
    if choice in exam_dates:
        exam_date = exam_dates[choice]
        time_remaining = exam_date - now
        days = time_remaining.days
        hours, remainder = divmod(time_remaining.total_seconds(), 3600)
        minutes, _ = divmod(remainder, 60)
        hours = int(hours)
        minutes = int(minutes)

        print(gradient_text(f"\n{choice} Exam Countdown\n🚀==========🚀\n  Days: {days}\n  Hours: {hours}\n  Minutes: {minutes}\n🚀==========🚀", start_rgb, end_rgb))
        print(gradient_text("\nGet revising!", start_rgb, end_rgb))
        print("   ✏📜️ \n")
        again = input(gradient_text("\nWould you like to check another subject? (yes/no): ", start_rgb, end_rgb)).strip().lower()
        if again != "yes":
            repeat = False  # Exit the loop

print("\nThank you for using this tool and feel free to support me on my GitHub and Discord ツ")
print("                           👇👇👇👇")
print("")
time.sleep(1)
print(gradient_text(f"💪 =======> https://github.com/OhnoMain <======= 💪", start_rgb, end_rgb))
print(gradient_text(f"🎮 =======> https://discord.gg/FgM4zAw4qP <======= 🎮", start_rgb, end_rgb))
time.sleep(2)
input("Press enter to exit: ")

         

