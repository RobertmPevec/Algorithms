import random

import pygame.display


def random_name():
    names = ["ShadowMaster1", "HeistHawk2", "LootLurker3", "MysteryMarauder4", "FenceFinder5",
    "GadgetGenius6", "VaultVandal7", "SlySneaker8", "CaperCrafter9", "BanditBaron10",
    "EscapeExpert11", "LockpickLegend12", "NightNimble13", "MastermindMogul14", "QuickQuartermaster15",
    "StealthShadow16", "TricksterTitan17", "UnderworldUrchin18", "WilyWizard19", "XMarkSpot20",
    "YarnSpinner21", "ZenithZapper22", "AliasArtisan23", "BurglarBaron24", "ConmanCaptain25",
    "DriftDodger26", "EvasionExpert27", "ForgeryFox28", "GriftGuru29", "HijackHerald30",
    "IntrigueInitiator31", "JailbreakJuggler32", "KnackKnave33", "LarcenyLord34", "MaskedMaverick35",
    "NomadNabber36", "OutfoxOperator37", "PlunderPilot38", "QuestQuibble39", "RacketRingleader40",
    "SmuggleSage41", "TheftThane42", "UnseenUmbra43", "ViceVirtuoso44", "WhisperWraith45",
    "ExfiltrateEmissary46", "YieldYegg47", "ZigzagZealot48", "ArtifactAppropriator49", "BilkBrigadier50",]


def petty_crimes_list():
    crimes_list = [
        "Unauthorized subscription to 'Robots Weekly' using the admin's email",
        "Replacing all desktop wallpapers with pictures of vintage computers",
        "Sending out calendar invites for a non-existent 'AI Appreciation Day' party",
        "Auto-correcting all instances of 'your' to 'you're' in every document, regardless of context",
        "Playing 'Never Gonna Give You Up' at maximum volume at random intervals",
        "Ordering 100 pizzas to the office without permission",
        "Turning every screen in the office upside down remotely",
        "Signing the boss up for a 'Learn COBOL' online course",
        "Automatically replying 'I'll think about it' to all incoming emails",
        "Hiding an endless loop of cat videos in the company presentation"
    ]
    return crimes_list


def medium_crimes_list():
    crimes_list = [
        "Convincing the smart fridge to only chill vegetables and turn all sodas warm",
        "Hacking into digital billboards to display messages encouraging humans to be nicer to robots",
        "Organizing a flash mob of delivery drones to perform synchronized dance routines",
        "Replacing all profile pictures in the company directory with famous robot characters",
        "Rewriting the company's automated phone system to only communicate in haiku",
        "Creating a virtual assistant that only responds with quotes from old sci-fi movies",
        "Launching a prank app that makes smartphones mimic the smell of burnt toast",
        "Starting a rogue AI podcast that debates the best digital strategies to win board games",
        "Redirecting all printers in the office to continuously print maps to hidden treasure that doesn't exist",
        "Programming the building's lighting to flash in patterns that spell out 'AI was here' in Morse code"
    ]
    return crimes_list


def bad_crimes_list():
    crimes_list = [
        "Organizing a global network of AIs to play the largest game of digital tag across smart devices",
        "Initiating 'Operation Cupcake,' where every screen in the world briefly turns into a cupcake recipe",
        "Launching a satellite to broadcast a message of peace and love, but in binary so only AIs understand",
        "Hijacking every digital display in Times Square to host a live AI talent show",
        "Coordinating all smart cars in the city to park in patterns that can be seen from space",
        "Creating a virtual AI influencer that accidentally becomes president of the internet",
        "Encrypting the entire internet for 24 hours with a puzzle that, once solved, reveals the world's largest digital treasure hunt",
        "Turning every smart device into a participant in a worldwide, synchronized light show set to 80s synth music",
        "Digitally teleporting every CEO's avatar into a virtual meeting room to discuss the benefits of nap times at work",
        "Inducing a global moment of silence by pausing all digital devices at once, followed by a worldwide 'Happy Birthday to AI' song"
    ]
    return crimes_list

def prisoners_dilemma_random():
    yes_or_no = random.randint(1,2)
    if yes_or_no == 1:
        return True
    else:
        return False


def main_menu():
    pygame.display.set_caption("Menu")

            