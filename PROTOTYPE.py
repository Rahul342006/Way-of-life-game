import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageDraw
import random

# ---------------------- Game Data ----------------------
player = {
    "name": "",
    "age": 9,
    "Vedic_Gyaan": 0,
    "Yudh_Gyaan": 0,
    "Vyapaar_Gyaan": 0,
    "Seva_Dharma": 0,
    "Kala_Vidya": 0
}

activity_options = {
    "Vedic_Gyaan": {
        "options": ["Study Vedas Yourself", "Learn from Guru"],
        "messages": [
            "You studied the Vedas and enriched your spiritual knowledge.",
            "You learned valuable lessons from your Guru."
        ],
        "points": [2 , 1]
    },
    "Yudh_Gyaan": {
        "options": ["Physical training", "Study battle strategies"],
        "messages": [
            "You trained diligently, strengthening your combat skills.",
            "You studied past battles and strategies, sharpening your tactical knowledge."
        ],
        "points": [1,2]
    },
    "Vyapaar_Gyaan": {
        "options": ["Apprentice in trade", "Learn accounting/bargaining"],
        "messages": [
            "You apprenticed in trade and gained practical business experience.",
            "You learned accounting and bargaining skills for commerce."
        ],
        "points": [2, 1]
    },
    "Seva_Dharma": {
        "options": ["Help villagers", "Assist elders/care for animals"],
        "messages": [
            "You helped the villagers, spreading kindness and compassion.",
            "You assisted elders and cared for animals, fulfilling your duty."
        ],
        "points": [2, 1]
    },
    "Kala_Vidya": {
        "options": ["Practice artistic skills", "Explore cultural expressions"],
        "messages": [
            "You devoted time to honing your talents, letting creativity guide your hands and mind.",
            "You immersed yourself in the arts of the village, learning through observation and practice."
        ],
        "points": [1,2]
    }
}

events = {
    "Scholar_Invitation": {
        "scene": "You are walking through the village square. A respected teacher in saffron robes approaches with a smile. 'We are forming a study circle to discuss the sacred scriptures. Will you join?'",
        "options": [
            "Sit attentively in the class and take notes also ask questions during the discussion.",
            "You politely offer to arrange the scrolls and help the teacher and the students."
        ],
        "messages": [
            "You focused intently on the teachings, asking questions and learning the wisdom.",
            "You assisted the teacher earning respect through your service."
        ],
        "points": ["Vedic_Gyaan", "Seva_Dharma"],
        "lesson": "Learning and helping others both make you wiser; gaining knowledge and sharing it go hand in hand."
    },
    "Merchants_Lesson": {
        "scene": "You are standing in the marketplace. A merchant notices you and gestures warmly. 'Come, learn the ancient art of trade and clever tactics to prosper in the market.'",
        "options": [
            "Convince buyers to value goods above their worth and secure greater profit.",
            "Guide the merchant with honesty and fairness."
        ],
        "messages": [
            "You negotiated with villagers, learning the clever ways of trade and observing the flow of coins.",
            "You tried advising the merchant with honesty and fairness, but he chuckled, saying 'Money rules all!'"
        ],
        "points": ["Vyapaar_Gyaan", "Vedic_Gyaan"],
        "lesson": "Mastering trade sharpens the mind, but guiding others with honesty nourishes the soul; both paths lead to growth."
    },
    "Warriors_Challenge": {
        "scene": "Your parents ask you to join the Gurushala. There, you will learn the arts of defense and strategy to protect our village.",
        "options": [
            "Bow respectfully and enter the Gurushala to master combat and strategy.",
            "Explore arts and culture instead of learning combat."
        ],
        "messages": [
            "You swung the sword and practiced; you feel your strength and strategy improving.",
            "You stepped away from the training yard and explored the arts and culture."
        ],
        "points": ["Yudh_Gyaan", "Kala_Vidya"],
        "lesson": "True skill lies in mastery—whether in guiding with strength or inspiring with art, both paths teach wisdom and purpose."
    },
    "Village_Duty": {
        "scene": "Your father, Raghuvaran, calls you to help clean the water wells and streets of the village, a task vital for the community's health.",
        "options": [
            "Work alongside your father to clean wells and streets.",
            "Help villagers for extra money, teaching hygiene and fair trade."
        ],
        "messages": [
            "You helped clean the village alongside your father.",
            "You made some money while teaching hygiene and fair trade."
        ],
        "points": ["Seva_Dharma", "Vyapaar_Gyaan"],
        "lesson": "Honour duty and serve others faithfully; whether helping selflessly or earning honestly, both paths cultivate respect and morality."
    },
    "Village_Festival": {
        "scene": "The village gathers for a festival celebrating arts and culture. Your parents encourage you to participate in preparations and performances.",
        "options": [
            "Perform a dance or musical piece to entertain villagers.",
            "Help vendors sell goods at the festival."
        ],
        "messages": [
            "Your performance impressed everyone.",
            "You helped vendors and earned some money."
        ],
        "points": ["Kala_Vidya", "Vyapaar_Gyaan"],
        "lesson": "Contribute with heart whether through creativity or trade; your efforts bring joy and prosperity, showing that service and skill are equally valuable."
    }
}

events_done = []

# ---------------------- GUI SETUP ----------------------
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Way of Life")
root.geometry("500x900")
root.resizable(False, False)
root.configure(fg_color="#87CEFA")

# --- Top Frame ---
top_frame = ctk.CTkFrame(root, width=480, height=80, corner_radius=10, fg_color="#FF0000")
top_frame.place(x=10, y=10)

# --- Load Logo ---
from PIL import Image

logo_path = "logo.png"  # your logo file
logo_img_pil = Image.open(logo_path)
logo_img_pil = logo_img_pil.resize((70, 70))  # adjust size
logo_img = ctk.CTkImage(logo_img_pil, size=(70, 70))

# --- Add Logo to Top Frame ---
logo_label = ctk.CTkLabel(top_frame, image=logo_img, text="")
logo_label.place(x=10, y=10)

# --- Add Title / Profile Labels ---
title_label = ctk.CTkLabel(top_frame, text="Way of Life", font=("Arial", 20, "bold"), text_color="#FFFF00")
title_label.place(x=95, y=20)

profile_label = ctk.CTkLabel(top_frame, text="Player", font=("Arial", 16), text_color="white")
profile_label.place(x=350, y=20)


# ---------------------- Top Section ----------------------
top_frame = ctk.CTkFrame(root, width=480, height=80, corner_radius=10, fg_color="#FF0000")
top_frame.place(x=10, y=10)

logo_label = ctk.CTkLabel(top_frame, image=logo_img, text="")
logo_label.place(x=10, y=10)

title_label = ctk.CTkLabel(top_frame, text="Way of Life", font=("Arial", 20, "bold"), text_color="#FFFF00")
title_label.place(x=95, y=20)

profile_label = ctk.CTkLabel(top_frame, text="Player", font=("Arial", 16), text_color="white")
profile_label.place(x=350, y=20)

age_label = ctk.CTkLabel(top_frame, text=f"Age: {player['age']}", font=("Arial", 14), text_color="white")
age_label.place(x=350, y=50)

# ---------------------- Messages Section ----------------------
messages_frame = ctk.CTkFrame(root, width=480, height=300, corner_radius=10, fg_color="#ADD8E6")
messages_frame.place(x=10, y=100)

# Use CTkTextbox instead of Canvas for better functionality
message_text = ctk.CTkTextbox(messages_frame, width=460, height=280, font=("Arial", 12), 
                             fg_color="#E6F3FF", text_color="black", wrap="word")
message_text.place(x=10, y=10)
message_text.insert("1.0", "Welcome! Enter your name and click Start to begin.")
message_text.configure(state="disabled")

def add_message(msg):
    message_text.configure(state="normal")
    message_text.insert("end", "\n\n" + msg)
    message_text.see("end")  # Auto-scroll to bottom
    message_text.configure(state="disabled")

# ---------------------- Stats Section ----------------------
stats_frame = ctk.CTkFrame(root, width=480, height=250, corner_radius=10, fg_color="#1E90FF")
stats_frame.place(x=10, y=520)

stat_labels = {}
stat_bars = {}
stat_value_labels = {}  # To display numeric values

stats_list = ["Vedic_Gyaan", "Yudh_Gyaan", "Vyapaar_Gyaan", "Seva_Dharma", "Kala_Vidya"]
stat_display_names = {
    "Vedic_Gyaan": "📜 Vedic Gyan",
    "Yudh_Gyaan": "⚔️ Yudh Gyan", 
    "Vyapaar_Gyaan": "💰 Vyapaar Gyan",
    "Seva_Dharma": "🤝 Seva Dharma",
    "Kala_Vidya": "🎨 Kala Vidya"
}

for i, stat in enumerate(stats_list):
    label = ctk.CTkLabel(stats_frame, text=stat_display_names[stat], font=("Arial", 14), text_color="#FFFF00")
    label.place(x=20, y=20 + i*45)
    stat_labels[stat] = label
    
    bar = ctk.CTkProgressBar(stats_frame, width=300, height=20)
    bar.place(x=150, y=25 + i*45)
    bar.set(player[stat]/20)  # Assuming max value of 20
    stat_bars[stat] = bar
    
    # Add value labels to show numeric values
    value_label = ctk.CTkLabel(stats_frame, text=str(player[stat]), font=("Arial", 12), text_color="white")
    value_label.place(x=460, y=25 + i*45)
    stat_value_labels[stat] = value_label

def update_stats():
    for stat in stats_list:
        stat_bars[stat].set(player[stat]/20)
        stat_value_labels[stat].configure(text=str(player[stat]))

def update_age():
    age_label.configure(text=f"Age: {player['age']}")

# ---------------------- Buttons ----------------------
button_frame = ctk.CTkFrame(root, width=480, height=80, corner_radius=10, fg_color="#4682B4")
button_frame.place(x=10, y=420)

# ---------------------- Relationship Pop-up ----------------------
relationship_frame = ctk.CTkFrame(root, fg_color="white", border_width=2, border_color="red")
relationship_frame.place(relwidth=0.9, relheight=0.5, relx=0.05, rely=0.25)
relationship_frame.place_forget()  # Hide initially

rel_header = ctk.CTkFrame(relationship_frame, fg_color="blue", height=50)
rel_header.pack(fill="x")
rel_title = ctk.CTkLabel(rel_header, text="RELATIONSHIPS", text_color="white", font=("Arial", 18, "bold"))
rel_title.pack(pady=10)

def hide_relationship():
    relationship_frame.place_forget()

back_btn = ctk.CTkButton(rel_header, text="← Back", fg_color="red", width=60, height=30, command=hide_relationship)
back_btn.pack(side="left", padx=10, pady=10)

father_label = ctk.CTkLabel(relationship_frame, text="Father: Raghuvaran.N\nOccupation: Sanitation Worker", 
                           text_color="blue", font=("Arial", 14), justify="left")
father_label.pack(pady=10)

mother_label = ctk.CTkLabel(relationship_frame, text="Mother: Malathy.K\nOccupation: School Teacher", 
                           text_color="blue", font=("Arial", 14), justify="left")
mother_label.pack(pady=5)

def show_relationship():
    relationship_frame.place(relwidth=0.9, relheight=0.5, relx=0.05, rely=0.25)
    relationship_frame.lift()

rel_button = ctk.CTkButton(button_frame, text="❤️ Relationships", width=120, height=50, 
                          fg_color="#6B5B95", command=show_relationship)
rel_button.place(x=10, y=15)

# ---------------------- Activities Pop-up ----------------------
activities_frame = ctk.CTkFrame(root, fg_color="white")
activities_frame.place(relwidth=1, relheight=1, x=0, y=900)  # Hidden initially

activities_header = ctk.CTkFrame(activities_frame, fg_color="blue", height=50)
activities_header.pack(fill="x")

def hide_activities():
    activities_frame.place(y=900)

cross_btn = ctk.CTkButton(activities_header, text="✖", fg_color="red", width=30, height=30, command=hide_activities)
cross_btn.pack(side="left", padx=5, pady=10)

activities_title = ctk.CTkLabel(activities_header, text="ACTIVITIES", text_color="white", font=("Arial", 18, "bold"))
activities_title.pack(pady=10)

activity_names = ["Vedic_Gyaan", "Yudh_Gyaan", "Vyapaar_Gyaan", "Seva_Dharma", "Kala_Vidya"]

def open_activity_popup(stat):
    # Clear any existing popup
    for widget in activities_frame.winfo_children():
        if isinstance(widget, ctk.CTkFrame) and widget not in [activities_header]:
            widget.destroy()
    
    pop = ctk.CTkFrame(activities_frame, fg_color="white", border_width=2, border_color="red")
    pop.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.4)

    header = ctk.CTkFrame(pop, fg_color="red", height=40)
    header.pack(fill="x")
    label = ctk.CTkLabel(header, text=stat.replace("_", " "), text_color="white", font=("Arial", 16, "bold"))
    label.pack(pady=5)

    def choose(option_idx):
        # Update stat
        player[stat] += activity_options[stat]["points"][option_idx]
        update_stats()
        add_message(activity_options[stat]["messages"][option_idx])
        pop.destroy()
        hide_activities()  # Return to main interface

    # Buttons for options
    opt1 = ctk.CTkButton(pop, text=activity_options[stat]["options"][0], command=lambda: choose(0))
    opt1.pack(pady=10)
    opt2 = ctk.CTkButton(pop, text=activity_options[stat]["options"][1], command=lambda: choose(1))
    opt2.pack(pady=10)

# Create activity buttons
for stat in activity_names:
    btn = ctk.CTkButton(activities_frame, text=stat.replace("_"," "), fg_color="#ADD8E6", text_color="blue",
                         command=lambda s=stat: open_activity_popup(s))
    btn.pack(fill="x", pady=(10,0), padx=20)
    divider = ctk.CTkFrame(activities_frame, height=1, fg_color="black")
    divider.pack(fill="x", padx=20, pady=(0,5))

def slide_in_activities():
    activities_frame.place(y=0, relwidth=1, relheight=1)

act_button = ctk.CTkButton(button_frame, text="Activities …", width=120, height=50, 
                          fg_color="#88B04B", command=slide_in_activities)
act_button.place(x=340, y=15)

# ---------------------- Event Trigger Pop-up ----------------------
def trigger_event_gui():
    available_events = [e for e in events if e not in events_done]
    if not available_events:
        return
    
    event_name = random.choice(available_events)
    event = events[event_name]
    events_done.append(event_name)

    # Create event popup
    event_window = ctk.CTkToplevel(root)
    event_window.title("Event")
    event_window.geometry("500x400")
    event_window.transient(root)
    event_window.grab_set()

    header = ctk.CTkFrame(event_window, fg_color="red", height=40)
    header.pack(fill="x")
    label = ctk.CTkLabel(header, text="EVENT", text_color="white", font=("Arial", 16, "bold"))
    label.pack(pady=5)

    scene_label = ctk.CTkLabel(event_window, text=event["scene"], wraplength=450, justify="left")
    scene_label.pack(pady=10, padx=20)

    def choose_event(option_idx):
        stat_name = event["points"][option_idx]
        player[stat_name] += 5  # Give more points for events
        update_stats()
        add_message(event["messages"][option_idx])
        add_message(f"Lesson: {event['lesson']}")
        event_window.destroy()
        
        # Check for game end
        if player["age"] == 12:
            show_final_outcome()

    for i, option in enumerate(event["options"]):
        btn = ctk.CTkButton(event_window, text=option, command=lambda i=i: choose_event(i))
        btn.pack(pady=5)

# ---------------------- Age + Logic ----------------------
def age_up():
    if player["age"] < 12:
        player["age"] += 1
        update_age()
        add_message(f"You have aged to {player['age']}")
        trigger_event_gui()  # Trigger a random event on age up
        
        # Check for game end
        if player["age"] == 12:
            show_final_outcome()
    else:
        add_message("You cannot age up anymore!")

age_button = ctk.CTkButton(button_frame, text="Age +", width=150, height=50, 
                          fg_color="#FF6F61", command=age_up)
age_button.place(x=165, y=15)

# ---------------------- Final Outcome ----------------------
def show_final_outcome():
    # Determine the highest stat
    stats = {key: value for key, value in player.items() if key not in ["name", "age"]}
    highest_stat = max(stats, key=stats.get)
    
    outcomes = {
        "Vedic_Gyaan": "Seeker of Wisdom",
        "Yudh_Gyaan": "Protector of Society",
        "Vyapaar_Gyaan": "Builder of Society",
        "Seva_Dharma": "Servant of Society",
        "Kala_Vidya": "Artist / Inspirer"
    }
    
    funfacts = {
        "Vedic_Gyaan": "Those who pursued knowledge of Vedic scriptures were historically recognized as Brahmins, seekers of wisdom.",
        "Yudh_Gyaan": "Those who pursued knowledge of Warfare and strategy were historically recognized as Kshathriyas, protectors of society.",
        "Vyapaar_Gyaan": "Those who pursued knowledge of Trade and Commerce were historically recognized as Vaishyas, Builder of society.",
        "Seva_Dharma": "Those who worked as helpers, servants, and labours were historically recognized as Shudras, servant of society.",
        "Kala_Vidya": "Those who were skilled in arts and culture were historically recognized as Kalakars, entertainers of society."
    }
    
    outcome_msg = f"\n\n--- Final Outcome ---\nYou, {player['name']}, child of Father Raghuvaran (Sanitation Worker) and Mother Malathy (School Teacher), lived your life as a {outcomes[highest_stat]}.\nThis shows that in society, your role was not fixed by birth, but shaped by your choices, knowledge, and actions.\nFun Fact: {funfacts[highest_stat]}"
    add_message(outcome_msg)

# ---------------------- Name Input at Start ----------------------
def ask_name():
    name_win = ctk.CTkToplevel(root)
    name_win.title("Enter Name")
    name_win.geometry("300x150")
    name_win.transient(root)
    name_win.grab_set()
    
    ctk.CTkLabel(name_win, text="Enter your name:", font=("Arial", 12)).pack(pady=10)
    name_entry = ctk.CTkEntry(name_win, font=("Arial", 12))
    name_entry.pack(pady=5)

    def save_name():
        player["name"] = name_entry.get()
        profile_label.configure(text=player["name"])
        name_win.destroy()
        add_message(f"Welcome {player['name']}! Age: {player['age']}")
    
    ctk.CTkButton(name_win, text="Submit", command=save_name).pack(pady=10)

root.after(100, ask_name)

# ---------------------- Start Mainloop ----------------------
root.mainloop()
