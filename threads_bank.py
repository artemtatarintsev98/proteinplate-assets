# Builds threads_bank.json: 60 ready Threads posts (30 days x 2) for busy women 25-45, moms, 35+, GLP-1 users.
# type: recipe (needs recipe_id: attach engine/img/<id>.jpg + recipe as reply chain), value, glp1, convo, story, soft
# Rules baked in: no medical/dosing advice, no invented results, real USDA-level numbers.
import json
FREE = "proteinplatehq.gumroad.com/l/free-grocery-list"
P = []
def add(t, text, rid=None): P.append({"type": t, "recipe_id": rid, "text": text.strip()})

# --- RECIPES (20) ---
add("recipe", "15-minute shrimp stir-fry. 43g protein.\n\nFaster than delivery, and nobody at the table asks \"is this healthy?\"\n\nFull recipe below 👇", "D2")
add("recipe", "Creamy Tuscan chicken. 51g protein per plate.\n\nTastes like a restaurant, made in one pan on a Tuesday.\n\nRecipe below 👇", "X13")
add("recipe", "Breakfast that keeps you full until lunch: cottage cheese egg bites. 33g protein.\n\nMake a batch Sunday, grab two every morning.\n\nRecipe 👇", "X1")
add("recipe", "Turkey smash tacos. 42g protein, 15 minutes.\n\nKids think it's taco night. You know it's a high-protein dinner.\n\nRecipe 👇", "D15")
add("recipe", "Egg fried cauliflower rice. 47g protein, 15 minutes, one pan.\n\nRecipe below 👇", "X18")
add("recipe", "Overnight oats that actually have protein in them. 26g.\n\n5 minutes tonight = breakfast done tomorrow.\n\nRecipe 👇", "B1")
add("recipe", "Steak burrito bowl. 45g protein.\n\nBuild-your-own bowls = everyone eats the same dinner, nobody complains.\n\nRecipe 👇", "X12")
add("recipe", "Lunch in 10 minutes: Mediterranean chicken wraps. 36g protein.\n\nRecipe 👇", "L7")
add("recipe", "Vegan and 45g protein? Tofu pad thai, lighter version.\n\nRecipe 👇", "V16")
add("recipe", "Honey garlic salmon bites. 35g protein, 20 minutes.\n\nThe one fish dinner picky eaters ask for again.\n\nRecipe 👇", "X15")
add("recipe", "Chicken parm meal prep. 51g protein per box.\n\n4 lunches, 35 minutes, zero thinking for the rest of the week.\n\nRecipe 👇", "X14")
add("recipe", "Small portion, big protein: Greek yogurt berry cup. 18g protein in a snack you can eat in 2 minutes.\n\nRecipe 👇", "S1")
add("recipe", "Garlic shrimp & spinach pasta. 44g protein, 20 minutes.\n\nPasta night doesn't have to mean a carb coma.\n\nRecipe 👇", "D10")
add("recipe", "Cottage cheese pizza bowl. 25g protein, 5 minutes, microwave.\n\nYes, it tastes like pizza. Recipe 👇", "X20")
add("recipe", "Sheet-pan lemon garlic chicken & potatoes. 42g protein.\n\nOne pan in the oven, 35 minutes, you do nothing.\n\nRecipe 👇", "D1")
add("recipe", "Protein French toast. 32g protein.\n\nWeekend breakfast that doesn't wreck your whole day.\n\nRecipe 👇", "X2")
add("recipe", "Seitan stir-fry. 41g protein, fully vegan, 15 minutes.\n\nRecipe 👇", "V12")
add("recipe", "Chocolate protein pudding. 19g protein, 3 minutes.\n\nFor the 9pm \"I need something sweet\" moment.\n\nRecipe 👇", "S7")
add("recipe", "One-pan chicken fried rice. 43g protein.\n\nBetter than takeout and you know exactly what's in it.\n\nRecipe 👇", "D13")
add("recipe", "Buffalo chicken salad. 40g protein, only 260 calories.\n\nA salad that actually fills you up. Recipe 👇", "X8")

# --- VALUE (12) ---
add("value", "How I hit ~120g protein without a single shake:\n\nBreakfast: 3 eggs + Greek yogurt → ~35g\nLunch: chicken wrap → ~36g\nSnack: cottage cheese → ~24g\nDinner: salmon or turkey → ~35g\n\nThat's it. Real food, 4 meals.")
add("value", "Cheap protein that's always in my kitchen:\n\n• Eggs\n• Cottage cheese\n• Greek yogurt\n• Canned tuna\n• Frozen shrimp\n• Lentils & black beans\n• Chicken thighs\n\nNone of it is fancy. All of it works.")
add("value", "Easiest swap I ever made: sour cream → plain Greek yogurt.\n\nSame creaminess on tacos and potatoes. About 3x the protein.")
add("value", "1 cup of cottage cheese ≈ 24g protein.\n1 cup of Greek yogurt ≈ 20g.\n1 can of tuna ≈ 25g.\n\nSome days hitting your protein is just knowing these three numbers.")
add("value", "If you're always hungry at 4pm, look at your lunch.\n\nSalad with no protein = snack attack in 2 hours.\nSame salad + chicken or chickpeas = full until dinner.")
add("value", "Meal prep doesn't need 5 hours on Sunday.\n\nWhat I actually do:\n1 tray of chicken in the oven\n1 pot of rice\n1 bag of frozen veg\n\n40 minutes. 4 lunches.")
add("value", "Protein at breakfast changed my whole day more than anything else.\n\nToast alone → hungry by 10.\nToast + 2 eggs + cottage cheese → fine until lunch.")
add("value", "Frozen shrimp is the most underrated weeknight dinner.\n\nThaws in 10 minutes under cold water, cooks in 4. ~24g protein per 100g.")
add("value", "Not a fan of meat? Protein still adds up:\n\nTofu (150g) ≈ 26g\nLentils (1 cup) ≈ 18g\nEdamame (1 cup) ≈ 18g\nSoy yogurt (high-protein) ≈ 14g\n\nVegan high-protein is very doable.")
add("value", "The family dinner rule that saved me:\n\nCook ONE protein for everyone. Kids add rice or pasta, I add extra veg.\n\nNo more cooking two dinners.")
add("value", "Snacks with 15g+ protein that take under 3 minutes:\n\n• Greek yogurt + berries\n• Cottage cheese + apple\n• Tuna on rice cakes\n• 2 boiled eggs + cheese stick")
add("value", "Biggest mistake I made for years: eating \"healthy\" but almost no protein.\n\nSalads, fruit, toast. Then wondering why I was starving and tired all the time.")

# --- GLP-1 (food only) (8) ---
add("glp1", "If you're on a GLP-1 and barely hungry, every bite has to count.\n\nSmall portions that still pack protein:\n• 1 cup Greek yogurt ≈ 20g\n• 2 eggs + cottage cheese ≈ 25g\n• Tuna on 2 rice cakes ≈ 22g\n\n(Food ideas only — your doctor sets your targets.)")
add("glp1", "On Ozempic/Wegovy/Mounjaro and can only eat a few bites?\n\nEat the protein first, then the rest. That's the whole trick most people share.\n\nWhat's your go-to small meal?")
add("glp1", "GLP-1 friendly snack: cottage cheese pizza bowl.\n\nTiny portion, ~25g protein, 5 minutes in the microwave.\n\nRecipe 👇", "X20")
add("glp1", "Small-appetite days: protein pudding.\n\nEasy to eat, ~19g protein, takes 3 minutes. Recipe 👇", "S7")
add("glp1", "People on GLP-1s keep asking me the same thing: \"how do I get protein when I'm never hungry?\"\n\nDrinkable and soft foods help: Greek yogurt, cottage cheese, eggs, soups with beans or chicken.\n\nAlways check targets with your doctor.")
add("glp1", "Food noise gone, appetite gone… and suddenly cooking feels pointless.\n\nAnyone else on a GLP-1 struggling to eat ENOUGH, not too much?")
add("glp1", "3 GLP-1 friendly mini-meals I'd make on low-appetite days:\n\n1. Greek yogurt + berries (18g)\n2. 2 eggs + toast (15g)\n3. Tuna rice cakes (22g)\n\nSmall, simple, protein first.")
add("glp1", "If you're on a GLP-1, what's the hardest part about food right now?\n\nA) Not hungry at all\nB) Nothing sounds good\nC) Getting enough protein\nD) Cooking for family when I barely eat")

# --- CONVERSATION (10) ---
add("convo", "Moms, honest question: what's the dinner you make when you're completely out of energy?")
add("convo", "What's harder for you?\n\nA) Breakfast\nB) Lunch at work\nC) Dinner for the family\nD) Not snacking at night")
add("convo", "Hot take: most \"healthy\" breakfasts are just dessert with good marketing.\n\nAgree or disagree?")
add("convo", "Cottage cheese: love it, hate it, or only when it's blended into something?")
add("convo", "What's one food you started eating more of and actually felt the difference?")
add("convo", "Be honest: how many times this year have you started a diet on a Monday?")
add("convo", "If someone gave you a week of dinners already planned, what would you still need to make it actually happen?")
add("convo", "What's the one meal your whole family agrees on? I'll turn the most popular answers into high-protein versions.")
add("convo", "Do you count protein, calories, or nothing at all?")
add("convo", "What's your 3pm snack? No judgment, I want real answers.")

# --- STORY (Artem's real story) (5) ---
add("story", "For years I ate badly and felt bad all the time.\n\nMy weight kept swinging. Too much, then too little, then too much again.\n\nWhat fixed it wasn't a diet. It was a simple plan: real food, protein in every meal.\n\nAnyone else been on that rollercoaster?")
add("story", "I didn't need more willpower. I needed to stop deciding what to eat 5 times a day.\n\nOnce I had a plan, the rest got easy.")
add("story", "I used to think eating healthy meant eating less.\n\nTurns out I was just eating the wrong things. More protein, real food, and I stopped feeling hungry and tired all day.")
add("story", "The day I stopped starting over every Monday was the day I wrote my meals down for the week.\n\nBoring? Yes. Works? Also yes.")
add("story", "My weight going up and down for years taught me one thing: anything too strict doesn't last.\n\nSimple meals I actually like, protein first. That's what stuck.")

# --- SOFT SELL (5) ---
add("soft", f"I put everything I buy for a ~120g protein week on one page.\n\nIt's free → {FREE}")
add("soft", f"Want my high-protein grocery list? Real food, no shakes, 3 sample days.\n\nFree here: {FREE}")
add("soft", "Too tired to think about dinner? I put my 7 fastest high-protein dinners in one PDF. 20 minutes each, 40+ g protein, one shopping list.\n\n$7 → proteinplatehq.gumroad.com/l/7-dinners")
add("soft", "I turned my plan into 30 days of simple high-protein meals with shopping lists for each week.\n\nIt's on my profile if you want it done for you.")
add("soft", "Sunday plan for a busy week: 7 dinners, 20 minutes each, all high-protein, one grocery run.\n\nIt's a $7 PDF: proteinplatehq.gumroad.com/l/7-dinners")

assert len(P) == 60, len(P)
# interleave so each day has a mix: slot A = recipe/value/glp1, slot B = convo/story/soft
A = [p for p in P if p["type"] in ("recipe", "value", "glp1")]
B = [p for p in P if p["type"] in ("convo", "story", "soft")]
A.sort(key=lambda p: {"recipe": 0, "value": 1, "glp1": 2}[p["type"]])
import itertools
def spread(lst, key):
    groups = {}
    for p in lst: groups.setdefault(p[key], []).append(p)
    out = []
    for row in itertools.zip_longest(*groups.values()):
        out += [x for x in row if x]
    return out
A, B = spread(A, "type"), spread(B, "type")
while len(B) < len(A): B.append(None)
bank = []
for i, (a, b) in enumerate(zip(A, B)):
    for slot, p in (("A", a), ("B", b)):
        if p: bank.append({"n": len(bank) + 1, "slot": slot, **p})
json.dump({"note": "Posts 1..N in order. Brain schedules unused ones, marks used in threads_bank_used.json.",
           "posts": bank}, open("threads_bank.json", "w"), indent=1, ensure_ascii=False)
print(len(bank), sum(1 for p in bank if p["slot"] == "A"), sum(1 for p in bank if p["slot"] == "B"))
