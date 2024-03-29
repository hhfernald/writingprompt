#!/usr/bin/env python

import random

class WritingPromptMaker():
    """Generate and return writing-prompt sentences."""
    
    personalities = [
        "abominable",
        "absurd",
        "accused",
        "active",
        "adventurous",
        "affectionate",
        "aggressive",
        "agoraphobic",
        "agreeable",
        "alarmed",
        "alert",
        "alluring",
        "ambitious",
        "amused",
        "angry",
        "anti-Semitic",
        "antisocial",
        "anxious",
        "apologetic",
        "appalled",
        "appalling",
        "appreciative",
        "apprehensive",
        "arrogant",
        "ascetic",
        "ashamed",
        "assertive",
        "asthmatic",
        "attention-seeking",
        "attentive",
        "attractive",
        "awe-inspring",
        "awesome",
        "awful",
        "bad",
        "banished",
        "beautiful",
        "befuddled",
        "bellicose",
        "belligerent",
        "bestial",
        "bigoted",
        "boastful",
        "boisterous",
        "bold",
        "bombastic",
        "bored",
        "bossy",
        "boyish",
        "brainy",
        "brash",
        "bratty",
        "brave",
        "brawny",
        "bright",
        "brown-nosing",
        "brutal",
        "brutish",
        "bullying",
        "burly",
        "bustling",
        "cagey",
        "callous",
        "calm",
        "campy",
        "candid",
        "capable",
        "carefree",
        "careful",
        "careless",
        "caring",
        "casual",
        "caustic",
        "cautious",
        "charming",
        "chaste",
        "cheating",
        "cheerful",
        "childish",
        "childlike",
        "claustrophobic",
        "clowning",
        "clumsy",
        "cold-hearted",
        "combative",
        "compassionate",
        "complaining",
        "compulsive",
        "concerned",
        "confident",
        "conniving",
        "cool-headed",
        "cooperative",
        "cosmopolitan",
        "courageous",
        "cowardly",
        "coy",
        "crabby",
        "crafty",
        "crass",
        "crazy",
        "creeping",
        "creepy",
        "crippled",
        "critical",
        "cruel",
        "cultured",
        "curious",
        "cynical",
        "dangerous",
        "dark",
        "daydreaming",
        "deceitful",
        "decisive",
        "dedicated",
        "defeated",
        "delicate",
        "delightful",
        "demonic",
        "depressed",
        "desperate",
        "deteriorating",
        "determined",
        "diligent",
        "dimwitted",
        "disagreeable",
        "diseased",
        "disinterested",
        "disreputable",
        "disrespectful",
        "dissatisfied",
        "distracted",
        "distrustful",
        "disturbed",
        "divisive",
        "docile",
        "domineering",
        "drunk",
        "dying",
        "dynamic",
        "eager",
        "eccentric",
        "effective",
        "efficient",
        "egocentric",
        "elegant",
        "elusive",
        "emotional",
        "enchanting",
        "energetic",
        "enthusiastic",
        "envious",
        "erudite",
        "evasive",
        "evil-minded",
        "excellent",
        "exhibitionistic",
        "fabulous",
        "fair",
        "faithful",
        "faithless",
        "fanatical",
        "fantastic",
        "far-sighted",
        "fastidious",
        "fast-talking",
        "fault-finding",
        "fearful",
        "fearless",
        "fiery",
        "fine",
        "foolish",
        "foppish",
        "foul-mouthed",
        "fragile",
        "frantic",
        "frazzled",
        "friendless",
        "friendly",
        "frightened",
        "frightening",
        "frowning",
        "frustrated",
        "fun-loving",
        "furtive",
        "fussy",
        "gabby",
        "garrulous",
        "generous",
        "gentle",
        "girlish",
        "glamorous",
        "gloating",
        "glorious",
        "gluttonous",
        "good-natured",
        "gorgeous",
        "gossipy",
        "gracious",
        "grateful",
        "greedy",
        "gregarious",
        "grieving",
        "grumpy",
        "guileless",
        "guilty",
        "happy",
        "hardened",
        "hard-drinking",
        "hard-working",
        "helpful",
        "helpless",
        "homeless",
        "homesick",
        "horny",
        "hostile",
        "huge",
        "humble",
        "hypochondriac",
        "hypocritical",
        "ignorant",
        "impartial",
        "impatient",
        "impish",
        "imprudent",
        "independent",
        "industrious",
        "infamous",
        "innovative",
        "inquisitive",
        "insistent",
        "insolent",
        "insomniac",
        "intelligent",
        "inventive",
        "irate",
        "iritated",
        "irrational",
        "irreverant",
        "jaded",
        "jealous",
        "jolly",
        "jumpy",
        "kind",
        "kind-hearted",
        "laconic",
        "laughing",
        "law-abiding",
        "lawless",
        "lazy",
        "leering",
        "likeable",
        "limber",
        "lissome",
        "listless",
        "lonely",
        "long-suffering",
        "long-winded",
        "loose-lipped",
        "lost",
        "loveless",
        "lovely",
        "loving",
        "lucky",
        "lustful",
        "mad",
        "magnanimous",
        "malevolent",
        "malicious",
        "masochistic",
        "maternal",
        "mature",
        "meddlesome",
        "meek",
        "messy",
        "militant",
        "miserly",
        "mocking",
        "morose",
        "mouthy",
        "mysterious",
        "nagging",
        "naive",
        "nameless",
        "narcissistic",
        "naughty",
        "nervous",
        "neurotic",
        "nice",
        "nitpicking",
        "noble",
        "noisy",
        "nosy",
        "obnoxious",
        "odd",
        "odious",
        "opportunistic",
        "ostracized",
        "otherworldly",
        "outrageous",
        "overbearing",
        "overprotective",
        "passionate",
        "paternal",
        "patronizing",
        "peaceful",
        "pedantic",
        "perky",
        "persevering",
        "persistent",
        "petulant",
        "philistine",
        "phony",
        "picky",
        "placid",
        "pleasant",
        "plucky",
        "poor",
        "preaching",
        "preening",
        "pretentious",
        "prickly",
        "proactive",
        "productive",
        "professional",
        "protective",
        "proud",
        "prudent",
        "prudish",
        "prying",
        "pugnacious",
        "punctual",
        "puritan",
        "quarrelsome",
        "querulous",
        "questioning",
        "quick",
        "quick-tempered",
        "quiet",
        "rabid",
        "racist",
        "radical",
        "rebellious",
        "recalcitrant",
        "receptive",
        "reflective",
        "reformed",
        "relentless",
        "religious",
        "remorseless",
        "renowned",
        "reputable",
        "resentful",
        "resigned",
        "resolute",
        "resourceful",
        "respectable",
        "respectful",
        "responsible",
        "retired",
        "reverent",
        "rich",
        "righteous",
        "romantic",
        "rudderless",
        "rude",
        "rustic",
        "sadistic",
        "sarcastic",
        "savage",
        "scandalous",
        "scoffing",
        "scornful",
        "scrupulous",
        "secretive",
        "sedentary",
        "self-centered",
        "self-righteous",
        "selfish",
        "sensitive",
        "sensual",
        "sentimental",
        "sex-starved",
        "silly",
        "simple-minded",
        "sincere",
        "sinful",
        "singing",
        "skeptical",
        "skinny",
        "sloppy",
        "slow",
        "sly",
        "sober",
        "soft-spoken",
        "solipsistic",
        "spiteful",
        "spoiled",
        "standoffish",
        "stealthy",
        "strong",
        "strong-willed",
        "stubborn",
        "subdued",
        "submissive",
        "successful",
        "suicidal",
        "sultry",
        "summoned",
        "suspicious",
        "sweet-natured",
        "sweet-talking",
        "sympathetic",
        "talented",
        "talkative",
        "tall",
        "tanned",
        "tasteful",
        "tender",
        "tepid",
        "terse",
        "testy",
        "thoughtful",
        "thoughtless",
        "timid",
        "tired",
        "tiresome",
        "tough",
        "treacherous",
        "troublemaking",
        "trusting",
        "trustworthy",
        "truthful",
        "tyrannical",
        "ugly",
        "unappreciated",
        "unappreciative",
        "unapproachable",
        "unassuming",
        "unattractive",
        "uncaring",
        "uncooperative",
        "unctuous",
        "understanding",
        "uneasy",
        "unflappable",
        "ungracious",
        "ungrateful",
        "unloved",
        "unlucky",
        "unmoved",
        "unnoticed",
        "unpopular",
        "unreasonable",
        "unscrupulous",
        "unseen",
        "unstable",
        "unwanted",
        "unwelcome",
        "upright",
        "uptight",
        "useless",
        "usurious",
        "vapid",
        "vengeful",
        "venomous",
        "vicious",
        "victorious",
        "vindicated",
        "vindictive",
        "violent",
        "virile",
        "virtue-signaling",
        "virtuous",
        "vivacious",
        "wandering",
        "warm-hearted",
        "wary",
        "wasted",
        "wasteful",
        "watchful",
        "wealthy",
        "weary",
        "well-dressed",
        "well-mannered",
        "well-to-do",
        "wise",
        "witty",
        "wonderful",
        "worried",
        "worsening",
        "worthless",
        "worthy",
        "wretched",
        "wry",
        "xenophobic",
        "yapping",
        "zealous",
    ]

    characters = [
        "administrator",
        "agent",
        "architect",
        "aristocrat",
        "associate",
        "astronaut",
        "auctioneer",
        "author",
        "banker",
        "botanist",
        "butler",
        "captain",
        "chef",
        "colonist",
        "commander",
        "criminal",
        "crook",
        "customer",
        "dancer",
        "demigod",
        "detective",
        "doctor",
        "drifter",
        "driver",
        "engineer",
        "farmer",
        "fiend",
        "fortune teller",
        "gadfly",
        "gangster",
        "gardener",
        "genie",
        "ghost",
        "goblin",
        "grifter",
        "harbor master",
        "hedonist",
        "hippy",
        "investigator",
        "jack-of-all-trades",
        "laborer",
        "librarian",
        "lieutenant",
        "lover",
        "magician",
        "mercenary",
        "musician",
        "mutant",
        "nomad",
        "number-cruncher",
        "officer",
        "official",
        "oracle",
        "organist",
        "outcast",
        "outlaw",
        "outsider",
        "pest",
        "pilot",
        "pirate",
        "politician",
        "police officer",
        "ruler",
        "scientist",
        "secretary",
        "security chief",
        "servant",
        "settler",
        "singer",
        "soldier",
        "soldier of fortune",
        "spy",
        "stranger",
        "teacher",
        "terrorist",
        "thief",
        "town gossip",
        "traveler",
        "veteran",
        "veterinarian",
        "village idiot",
        "warrior",
        "worker",
        "zealot",
        "{cm}",
        "{cf}",
    ]

    male_characters = [
        "antihero",
        "bachelor",
        "baron",
        "boy",
        "brother",
        "chairman",
        "chieftain",
        "count",
        "cowboy",
        "demigod",
        "duke",
        "father",
        "gentleman",
        "giant",
        "god",
        "grandfather",
        "groom",
        "handyman",
        "hero",
        "horseman",
        "husband",
        "king",
        "knight",
        "lord",
        "man",
        "overlord",
        "patriarch",
        "playboy",
        "priest",
        "son",
        "uncle",
        "widower",
    ]

    female_characters = [
        "actress",
        "aunt",
        "baroness",
        "bride",
        "bridesmaid",
        "countess",
        "cowgirl",
        "daughter",
        "duchess",
        "giantess",
        "girl",
        "goddess",
        "grandmother",
        "heroine",
        "lady",
        "maiden",
        "matriarch",
        "matron",
        "mother",
        "nun",
        "priestess",
        "princess",
        "queen",
        "sister",
        "spinster",
        "tomboy",
        "wench",
        "widow",
        "wife",
        "woman",
    ]

    character_verbs = [
        "accept {pp} offer",
        "apologize to {po}",
        "ask {po}",
        "ask {po} some hard questions",
        "ask {po} to wait",
        "attack {po}",
        "avenge {po}",
        "beat the tar out of {po}",
        "befriend {po}",
        "beg {po} for forgiveness",
        "berate {po}",
        "break {po} like a twig",
        "break {pp} heart",
        "break {pp} neck",
        "break up {pp} marriage",
        "bring {po} to justice",
        "bring vengeance upon {po}",
        "capture {po}",
        "challenge {po} to a contest",
        "check on {po}",
        "chew {po} out",
        "confess to {po}",
        "confront {po}",
        "correct {po}",
        "crush {po}",
        "crush {pp} enemies",
        "cure {po}",
        "defend {po}",
        "destroy {po}",
        "drag {po} back home",
        "fire {po}",
        "get {pp} advice",
        "get {po} the help {ps} needed",
        "give {po} a piece of {pp} mind",
        "hire {po}",
        "humiliate {pp} in public",
        "infect {pp} with a disease",
        "invite {po} to a get-together",
        "invite {po} to a party",
        "join {pp} cause",
        "kick {po} out of the house",
        "kidnap {po}",
        "kill {po}",
        "lay a curse upon {po}",
        "make {po} an offer",
        "make {po} stop",
        "negotiate with {po}",
        "offer {po} a contract",
        "play a prank on {po}",
        "propose to {po}",
        "prosecute {po}",
        "protect {po}",
        "quarrel with {po}",
        "regain {pp} trust",
        "rekindle the relationship with {po}",
        "rescue {po}",
        "rescue {pp} friends",
        "rough {po} up",
        "ruin {po} financially",
        "scare {po}",
        "seek {pp} counsel",
        "settle down with {po}",
        "sit down with {po}",
        "slap {po}",
        "sleep with {po}",
        "spit on {po}",
        "straighten {po} out",
        "swear an oath to {po}",
        "swindle {po}",
        "teach {po} a lesson",
        "tell {po} to hurry up",
        "track {po} down",
    ]

    object_verbs = [
        "analyze",
        "bring back",
        "buy",
        "capture",
        "carry",
        "destroy",
        "dismantle",
        "examine",
        "find the owner of",
        "manufacture",
        "produce",
        "rebuild",
        "reclaim",
        "reconstruct",
        "repair",
        "sabotage",
        "seize",
        "sell",
        "steal",
    ]

    objects = [
        "artifact",
        "book",
        "box",
        "car",
        "casket",
        "chalice",
        "engine",
        "gun",
        "icon",
        "landrover",
        "machine",
        "motor",
        "painting",
        "portal",
        "probe",
        "reactor",
        "robot",
        "ship",
        "statue",
        "truck",
        "vessel",
        "weapon",
    ]

    settings = [
        "airport",
        "attic",
        "balcony",
        "ballroom",
        "basement",
        "bay",
        "beach",
        "bus",
        "camp",
        "castle",
        "cathedral",
        "cave",
        "cellar",
        "chamber",
        "church",
        "city hall",
        "cockpit",
        "coffeehouse",
        "colony",
        "compartment",
        "corridor",
        "courtroom",
        "courtyard",
        "cruise ship",
        "den",
        "elevator",
        "field",
        "forest",
        "fortress",
        "garden",
        "glacier",
        "greenhouse",
        "grotto",
        "hall",
        "haven",
        "highway",
        "hotel",
        "hothouse",
        "house",
        "inn",
        "jungle",
        "lab",
        "lighthouse",
        "mall",
        "meadow",
        "mountain pass",
        "museum",
        "palace",
        "park",
        "pasture",
        "pavilion",
        "penthouse",
        "prison",
        "riverbed",
        "room",
        "school",
        "space station",
        "stable",
        "store",
        "street",
        "subway",
        "tavern",
        "temple",
        "theater",
        "tower",
        "tunnel",
        "valley",
    ]

    setting_adjectives = [
        "abandoned",
        "bustling",
        "clean",
        "closed",
        "cold",
        "colorful",
        "crowded",
        "crumbling",
        "damp",
        "dangerous",
        "dank",
        "dark",
        "decaying",
        "deserted",
        "dry",
        "dusty",
        "east",
        "echoing",
        "elegant",
        "filthy",
        "flooded",
        "forbidden",
        "gloomy",
        "high",
        "hot",
        "infested",
        "long",
        "low",
        "magnificent",
        "mighty",
        "mildewy",
        "monstrous",
        "muddy",
        "musty",
        "noisy",
        "north",
        "ominous",
        "ornamental",
        "ornate",
        "plain",
        "quiet",
        "remote",
        "rustic",
        "shadowy",
        "sordid",
        "south",
        "stuffy",
        "sunny",
        "tidy",
        "well-maintained",
        "west",
        "wide",
    ]

    setting_gerunds = [
        "entering",
        "exiting",
        "exploring",
        "hiding in",
        "investigating",
        "searching for",
        "seeking to escape",
        "staying in",
        "walking in",
    ]

    sounds = [
        "babbling",
        "a bell tolling",
        "the bell ringing",
        "chanting",
        "clanging",
        "cries of anguish",
        "a cry for help",
        "a cry of terror",
        "the distant baying of hounds",
        "a distant rumbling",
        "a dog barking",
        "an engine starting",
        "a ferocious banging",
        "growling",
        "a howl of rage",
        "laughter",
        "a man and a woman quarrelling",
        "a man barking orders",
        "muttering",
        "scratching or gnawing",
        "a shriek, then silence",
        "singing",
        "someone calling {pp} name",
        "squeaking",
        "ululations",
        "the warning honks of moving trucks",
        "the whirring of machinery",
    ]

    templates = [
        "While {sg} the {sa} {se}, the {pe} {ch} heard {so}.",
        "The {pe} {ch} wanted to find the {ch} and {cv}.",
        "The {pe} {ch} had been hired to {ov} the {ob}.",
        "Who was that {pe} {ch}?",
        "What was that {pe} {ch} doing in the {sa} {se}?",
        "Find the {ch} before {ps} decides to {cv}.",
        "I had to find that {pe} {ch} and {cv}.",
        "I was to help the {pe} {ch} in the {sa} {se} to {ov} the {ob}.",
        "No one wanted to {cv}, the {pe} {ch}.",
    ]
    
    def __init__(self):
        self.nounlists = [self.characters, self.female_characters,
                          self.male_characters, self.objects, self.settings]

    def _fill(self, t):
        """Convert a template into a random sentence; return the sentence."""
        
        t = t.replace("{sg}", random.choice(self.setting_gerunds), 1)
        t = t.replace("{sa}", random.choice(self.setting_adjectives), 1)
        t = t.replace("{se}", random.choice(self.settings), 1)
        t = t.replace("{pe}", random.choice(self.personalities), 1)
        t = t.replace("{so}", random.choice(self.sounds), 1)
        t = t.replace("{cv}", random.choice(self.character_verbs), 1)
        t = t.replace("{ov}", random.choice(self.object_verbs), 1)
        t = t.replace("{ob}", random.choice(self.objects), 1)

        # Characters and pronouns:

        t = t.replace("{ch}", random.choice(self.characters), 1)

        if t.count("{cm}"):
            t = t.replace("{ps}", "he")  # subject pronoun
            t = t.replace("{po}", "him") # object pronoun
            t = t.replace("{pp}", "his") # possessive pronoun
        elif t.count("{cf}"):
            t = t.replace("{ps}", "she")
            t = t.replace("{po}", "her")
            t = t.replace("{pp}", "her")
        else:
            t = t.replace("{ps}", random.choice(["he", "she"]))
            t = t.replace("{po}", random.choice(["him", "her"]))
            t = t.replace("{pp}", random.choice(["his", "her"]))

        t = t.replace("{cm}", random.choice(self.male_characters), 1)
        t = t.replace("{cf}", random.choice(self.female_characters), 1)

        return t
    
    def noun(self):
        '''Return a randomly selected noun.'''
        nounlist = random.choice(self.nounlists)
        noun = '{}'
        while '{' in noun:
            noun = random.choice(nounlist)
        return noun

    def prompt(self):
        '''Return a randomly generated writing prompt (sentence).'''
        
        t = random.choice(self.templates)

        while "{" in t:
            t = self._fill(t)

        return t

if __name__ == '__main__':
    # Print ten writing prompts.
    m = WritingPromptMaker()
    for i in range(10):
        print(m.prompt())

