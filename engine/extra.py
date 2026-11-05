# Extra recipes for the content engine (Reels/Shorts/stories). NOT part of the $27 PDF (WEEKS untouched).
# Separate list XR (does not touch data.R, so build.py/PDF stays unchanged). Macros in XM.
# X* = regular, V* = vegan. Image: img/<id>.jpg. Prompts for image generation in PHOTO.
from data import ING
XR = []
def rec(id, name, meal, mins, serves, ings, steps, swap="", tip=""):
    XR.append(dict(id=id, name=name, meal=meal, mins=mins, serves=serves, ings=ings, steps=steps, swap=swap, tip=tip))

ING.update({
 "pork tenderloin":            (143, 26.0, 0, 3.5, "Meat & Fish"),
 "sirloin steak, lean":        (150, 23.0, 0, 6.0, "Meat & Fish"),
 "chicken sausage":            (150, 15.0, 3.0, 8.0, "Meat & Fish"),
 "part-skim ricotta":          (138, 11.4, 5.1, 7.9, "Dairy & Eggs"),
 "light cheddar, shredded":    (290, 28.0, 2.0, 18.0, "Dairy & Eggs"),
 "extra-firm tofu":            (144, 17.3, 2.8, 8.7, "Produce"),
 "silken tofu":                (55, 4.8, 2.9, 2.7, "Produce"),
 "tempeh":                     (192, 20.3, 7.6, 10.8, "Produce"),
 "seitan":                     (140, 25.0, 6.0, 2.0, "Produce"),
 "unsweetened soy milk":       (33, 2.9, 1.7, 1.6, "Dairy & Eggs"),
 "high-protein soy yogurt":    (75, 7.0, 4.0, 3.0, "Dairy & Eggs"),
 "pea protein powder (vanilla)": (380, 78.0, 6.0, 6.0, "Pantry"),
 "nutritional yeast":          (325, 50.0, 36.0, 4.0, "Pantry"),
 "hemp seeds":                 (553, 31.6, 8.7, 48.8, "Pantry"),
 "pumpkin seeds":              (559, 30.2, 10.7, 49.1, "Pantry"),
 "red lentil pasta (dry)":     (340, 25.0, 58.0, 2.0, "Pantry"),
 "tahini":                     (595, 17.0, 21.0, 54.0, "Pantry"),
 "kale":                       (35, 2.9, 4.4, 1.5, "Produce"),
 "cauliflower":                (25, 1.9, 5.0, 0.3, "Produce"),
 "frozen peas":                (77, 5.2, 13.6, 0.4, "Frozen"),
 "mango":                      (60, 0.8, 15.0, 0.4, "Produce"),
 "canned diced tomatoes":      (32, 1.6, 7.0, 0.3, "Pantry"),
 "corn tortilla":              (218, 5.7, 44.6, 2.9, "Bakery"),
 "maple syrup":                (260, 0, 67.0, 0, "Pantry"),
 "canned white beans, drained": (114, 7.3, 20.4, 0.3, "Pantry"),
})

# ---------------- REGULAR ----------------
rec("X1","Cottage Cheese Egg Bites","Breakfast",25,2,
 [("eggs",100),("low-fat cottage cheese (2%)",100),("spinach",30),("light cheddar, shredded",15),("whole wheat bread",35)],
 ["Blend eggs and cottage cheese until smooth.","Pour into a greased muffin tin over chopped spinach, top with cheddar.","Bake at 350°F / 175°C for 20 min. Serve with toast."],
 tip="Starbucks-style bites for a fraction of the price.")
rec("X2","Protein French Toast","Breakfast",12,1,
 [("whole wheat bread",70),("egg whites (carton)",120),("skim milk",50),("frozen mixed berries",80),("nonfat Greek yogurt",80),("maple syrup",8)],
 ["Whisk egg whites, milk and cinnamon.","Soak bread 20 sec per side, cook in a non-stick pan 2–3 min per side.","Top with Greek yogurt, warmed berries and maple syrup."])
rec("X3","Breakfast Hash with Turkey Sausage","Breakfast",20,2,
 [("chicken sausage",80),("potatoes",150),("bell pepper",60),("eggs",100),("olive oil",4)],
 ["Dice potatoes small, cook in oil 10 min until crispy.","Add sliced sausage and pepper, cook 4 min.","Make two wells, crack in eggs, cover 4 min."])
rec("X4","Ricotta Berry Toast","Breakfast",5,1,
 [("whole wheat bread",70),("part-skim ricotta",100),("nonfat Greek yogurt",60),("frozen mixed berries",60),("honey",5)],
 ["Mix ricotta with Greek yogurt and a pinch of salt.","Spread on toast, top with berries and honey."])
rec("X5","Steak & Egg Breakfast Tacos","Breakfast",15,2,
 [("sirloin steak, lean",90),("eggs",50),("corn tortilla",50),("salsa",40),("avocado",20)],
 ["Sear thin-sliced steak with salt and cumin 2 min.","Scramble egg in the same pan.","Fill warm tortillas with steak, egg, salsa and avocado."])
rec("X6","Chicken Caesar Wrap (Greek Yogurt Dressing)","Lunch",10,1,
 [("whole wheat tortilla",45),("chicken breast",130),("mixed salad greens",50),("nonfat Greek yogurt",40),("parmesan, grated",10),("lemon juice",10)],
 ["Stir yogurt, lemon, parmesan, garlic and pepper into a dressing.","Toss greens and sliced cooked chicken with the dressing.","Wrap tightly, cut in half."])
rec("X7","Pork Tenderloin Rice Bowls","Lunch",30,4,
 [("pork tenderloin",140),("cooked brown rice",110),("broccoli",100),("carrots",40),("low-sodium soy sauce",15),("honey",5)],
 ["Rub pork with garlic, paprika, salt. Roast at 425°F / 220°C for 20 min, rest 5.","Steam broccoli and carrots.","Slice pork, divide over rice and veg, drizzle soy-honey glaze."],
 tip="Pork tenderloin is as lean as chicken breast.")
rec("X8","Buffalo Chicken Salad","Lunch",15,2,
 [("chicken breast",140),("mixed salad greens",60),("carrots",40),("cucumber",50),("nonfat Greek yogurt",40),("pickled jalapeños / hot sauce",20),("light cheddar, shredded",10)],
 ["Toss cooked chicken in hot sauce.","Mix yogurt with garlic, dill and lemon for a ranch-style dressing.","Build salad: greens, veg, buffalo chicken, cheese, dressing."])
rec("X9","Tuna Melt Stuffed Peppers","Lunch",20,2,
 [("canned tuna in water, drained",110),("bell pepper",150),("nonfat Greek yogurt",30),("light cheddar, shredded",20),("red onion",15)],
 ["Mix tuna, yogurt, diced onion, mustard and pepper.","Fill pepper halves, top with cheddar.","Bake at 400°F / 200°C for 12 min."])
rec("X10","Chicken Shawarma Bowls","Lunch",30,4,
 [("chicken thigh, boneless skinless",150),("cooked quinoa",110),("cucumber",60),("cherry tomatoes",60),("tzatziki",40),("red onion",15)],
 ["Toss chicken with cumin, paprika, turmeric, garlic, lemon. Roast at 425°F / 220°C for 22 min.","Chop salad veg.","Divide quinoa, chicken, veg and tzatziki into 4 containers."])
rec("X11","Shrimp Tacos with Mango Salsa","Dinner",20,2,
 [("shrimp, peeled",160),("corn tortilla",60),("mango",60),("red onion",15),("avocado",25),("nonfat Greek yogurt",30)],
 ["Season shrimp with chili and lime, sear 2 min per side.","Dice mango and onion with lime and salt.","Fill tortillas with shrimp, salsa, avocado and a spoon of yogurt."])
rec("X12","Steak Burrito Bowl","Dinner",25,2,
 [("sirloin steak, lean",150),("cooked white rice",100),("canned black beans, drained",60),("frozen corn",40),("salsa",40),("mixed salad greens",30)],
 ["Season steak with cumin, chili, salt. Sear 3–4 min per side, rest and slice.","Warm beans and corn.","Bowl: rice, greens, beans, corn, steak, salsa."])
rec("X13","Creamy Tuscan Chicken","Dinner",25,3,
 [("chicken breast",160),("spinach",60),("cherry tomatoes",80),("part-skim ricotta",50),("parmesan, grated",8),("cooked quinoa",100),("olive oil",4)],
 ["Sear seasoned chicken 5–6 min per side, remove.","Cook garlic and tomatoes 3 min, stir in ricotta, parmesan and a splash of water.","Wilt spinach, return chicken. Serve over quinoa."])
rec("X14","Chicken Parm Meal Prep","Dinner",35,4,
 [("chicken breast",150),("marinara sauce",80),("part-skim mozzarella",25),("whole wheat pasta (dry)",50),("broccoli",100)],
 ["Pound chicken thin, season, bake at 425°F / 220°C for 15 min.","Top with marinara and mozzarella, bake 5 more min.","Serve with pasta and steamed broccoli."])
rec("X15","Honey Garlic Salmon Bites","Dinner",20,2,
 [("salmon fillet",140),("cooked white rice",110),("green beans",120),("honey",8),("low-sodium soy sauce",12),("garlic",5)],
 ["Cube salmon, sear 2 min per side.","Add garlic, honey and soy, toss 1 min until sticky.","Serve over rice with green beans."])
rec("X16","Turkey Bolognese","Dinner",30,4,
 [("ground turkey (93% lean)",130),("canned diced tomatoes",120),("carrots",40),("red onion",30),("whole wheat pasta (dry)",60),("parmesan, grated",6)],
 ["Brown turkey with onion and grated carrot 8 min.","Add tomatoes, Italian herbs, salt. Simmer 15 min.","Toss with pasta, finish with parmesan."],
 tip="Freezes for 3 months.")
rec("X17","Greek Chicken Sheet-Pan Gyros","Dinner",30,2,
 [("chicken breast",150),("whole wheat pita",64),("tzatziki",40),("cherry tomatoes",50),("red onion",20),("cucumber",50)],
 ["Toss chicken strips with oregano, lemon, garlic. Roast at 425°F / 220°C for 18 min.","Warm pitas.","Fill with chicken, tzatziki, tomato, onion, cucumber."])
rec("X18","Egg Fried Cauliflower Rice","Dinner",15,2,
 [("chicken breast",120),("cauliflower",200),("eggs",100),("frozen peas",50),("carrots",30),("low-sodium soy sauce",15),("olive oil",4)],
 ["Pulse cauliflower into rice.","Cook diced chicken in oil 6 min, push aside, scramble eggs.","Add cauliflower, peas, carrot, soy. Stir-fry 5 min."])
rec("X19","Protein Cookie Dough Dip","Snack",5,1,
 [("nonfat Greek yogurt",150),("peanut butter",10),("dark chocolate chips",6),("maple syrup",6)],
 ["Stir yogurt, peanut butter, maple syrup and a pinch of salt.","Fold in chocolate chips. Eat with apple slices."],
 tip="Dessert that's actually a snack.")
rec("X20","Cottage Cheese Pizza Bowl","Snack",5,1,
 [("low-fat cottage cheese (2%)",150),("marinara sauce",40),("part-skim mozzarella",15),("turkey breast deli slices",30)],
 ["Layer cottage cheese, marinara, chopped turkey and mozzarella in a bowl.","Microwave 60–90 sec until melty. Oregano on top."])

# ---------------- VEGAN ----------------
rec("V1","Tofu Scramble Breakfast Burrito","Breakfast",15,1,
 [("extra-firm tofu",150),("whole wheat tortilla",45),("canned black beans, drained",40),("spinach",30),("salsa",30),("nutritional yeast",5)],
 ["Crumble tofu into a hot pan with turmeric, garlic powder, salt. Cook 5 min.","Add spinach and nutritional yeast.","Wrap with beans and salsa in a warm tortilla."])
rec("V2","Vanilla Protein Overnight Oats (Vegan)","Breakfast",5,1,
 [("rolled oats",45),("unsweetened soy milk",200),("pea protein powder (vanilla)",20),("chia seeds",8),("frozen mixed berries",70)],
 ["Shake oats, soy milk, protein powder and chia in a jar.","Top with berries, refrigerate overnight.","Eat cold or warm 60 sec."])
rec("V3","Silken Tofu Veggie Omelette","Breakfast",15,1,
 [("silken tofu",200),("nutritional yeast",8),("mushrooms",60),("spinach",30),("whole wheat bread",35)],
 ["Blend silken tofu, nutritional yeast, turmeric, salt into a batter.","Pour into a hot oiled pan over sautéed mushrooms and spinach, cover 6 min.","Fold and serve with toast."])
rec("V4","Peanut Butter Soy Yogurt Bowl","Breakfast",3,1,
 [("high-protein soy yogurt",200),("pea protein powder (vanilla)",10),("peanut butter",12),("banana",60),("hemp seeds",10),("granola",15)],
 ["Stir protein powder into soy yogurt.","Top with banana, peanut butter, hemp seeds and granola."])
rec("V5","Blueberry Protein Pancakes (Vegan)","Breakfast",15,1,
 [("rolled oats",40),("unsweetened soy milk",120),("pea protein powder (vanilla)",20),("banana",50),("frozen mixed berries",50),("maple syrup",8)],
 ["Blend oats, soy milk, protein powder and banana.","Cook small pancakes 2 min per side, dropping berries on top.","Finish with maple syrup."])
rec("V6","Crispy Tofu Rice Bowls","Lunch",30,4,
 [("extra-firm tofu",180),("cooked brown rice",110),("edamame, shelled (frozen)",40),("carrots",40),("cucumber",50),("low-sodium soy sauce",15)],
 ["Press tofu, cube, toss with soy and cornstarch. Bake at 425°F / 220°C for 25 min.","Steam edamame, slice veg.","Divide rice, tofu, veg into containers."])
rec("V7","Lentil Taco Bowls","Lunch",25,4,
 [("cooked lentils",220),("cooked white rice",70),("canned black beans, drained",50),("salsa",50),("avocado",30),("mixed salad greens",30)],
 ["Sauté lentils with taco spices and a splash of water 5 min, mash lightly.","Warm beans.","Bowl: rice, greens, lentil taco meat, beans, salsa, avocado."])
rec("V8","Tempeh BLT-Style Sandwich","Lunch",15,1,
 [("tempeh",100),("whole wheat bread",70),("cherry tomatoes",50),("mixed salad greens",30),("hummus",30),("maple syrup",5)],
 ["Slice tempeh thin, pan-fry with soy, maple and smoked paprika 3 min per side.","Spread hummus on toast.","Layer tempeh, greens and tomato."])
rec("V9","Chickpea 'Tuna' Salad Wrap","Lunch",10,1,
 [("canned chickpeas, drained",150),("extra-firm tofu",60),("tahini",10),("whole wheat tortilla",45),("cucumber",40),("red onion",15),("lemon juice",10),("hemp seeds",10)],
 ["Mash chickpeas and crumbled tofu with tahini, lemon, mustard, salt.","Mix in diced onion, cucumber and hemp seeds.","Wrap in a tortilla."])
rec("V10","Peanut Tempeh Noodle Salad","Lunch",20,3,
 [("tempeh",110),("red lentil pasta (dry)",50),("carrots",40),("cucumber",50),("peanut butter",12),("low-sodium soy sauce",12)],
 ["Cook pasta, rinse cold.","Cube and pan-fry tempeh 6 min.","Whisk peanut butter, soy, lime and water; toss everything."])
rec("V11","Red Lentil Pasta Bolognese","Dinner",25,3,
 [("red lentil pasta (dry)",75),("cooked lentils",80),("canned diced tomatoes",120),("carrots",40),("red onion",30),("nutritional yeast",5)],
 ["Cook onion and grated carrot 5 min, add lentils and tomatoes, simmer 12 min.","Cook pasta.","Toss together, top with nutritional yeast."],
 tip="Lentil pasta = double the protein of regular pasta.")
rec("V12","Seitan Stir-Fry","Dinner",15,2,
 [("seitan",130),("frozen stir-fry vegetables",200),("cooked white rice",110),("low-sodium soy sauce",15),("garlic",5),("olive oil",4)],
 ["Sear sliced seitan in oil 3 min.","Add vegetables and garlic, stir-fry 5 min.","Add soy sauce, serve over rice."])
rec("V13","Chickpea Coconut Curry","Dinner",25,4,
 [("canned chickpeas, drained",130),("extra-firm tofu",80),("light coconut milk",60),("curry paste",12),("spinach",60),("cooked brown rice",100)],
 ["Fry curry paste 1 min, add coconut milk and 1/2 cup water.","Add chickpeas and cubed tofu, simmer 12 min.","Wilt spinach, serve over rice."])
rec("V14","BBQ Tempeh Sheet Pan","Dinner",30,2,
 [("tempeh",120),("sweet potato",150),("broccoli",150),("olive oil",5),("maple syrup",6)],
 ["Cube sweet potato, roast at 425°F / 220°C for 12 min.","Add tempeh tossed in BBQ spices + maple, and broccoli.","Roast 15 more minutes."])
rec("V15","Black Bean Tofu Tacos","Dinner",20,2,
 [("extra-firm tofu",120),("canned black beans, drained",80),("corn tortilla",60),("salsa",40),("avocado",25),("mixed salad greens",30)],
 ["Crumble tofu with taco spices, cook until crispy 8 min.","Warm beans and tortillas.","Fill with tofu, beans, greens, salsa, avocado."])
rec("V16","Tofu Pad Thai (Lighter)","Dinner",20,2,
 [("extra-firm tofu",150),("red lentil pasta (dry)",50),("frozen stir-fry vegetables",120),("peanut butter",10),("low-sodium soy sauce",15),("lemon juice",10)],
 ["Pan-fry tofu cubes until golden.","Cook pasta, stir-fry vegetables.","Toss with a sauce of peanut butter, soy, lime/lemon and chili."])
rec("V17","White Bean & Kale Pasta","Dinner",20,2,
 [("red lentil pasta (dry)",60),("canned white beans, drained",120),("kale",60),("garlic",6),("olive oil",6),("nutritional yeast",6)],
 ["Cook pasta, keep 1/2 cup water.","Sauté garlic in oil, add beans and kale 4 min.","Toss with pasta, pasta water, nutritional yeast, lemon."])
rec("V18","Teriyaki Tofu & Edamame Bowls","Dinner",25,2,
 [("extra-firm tofu",160),("edamame, shelled (frozen)",60),("cooked white rice",110),("broccoli",100),("teriyaki sauce",15)],
 ["Bake cubed tofu at 425°F / 220°C for 20 min.","Toss with teriyaki.","Serve over rice with edamame and broccoli."])
rec("V19","Chocolate Protein Mousse (Silken Tofu)","Snack",5,2,
 [("silken tofu",150),("cocoa powder (unsweetened)",8),("pea protein powder (vanilla)",10),("maple syrup",10)],
 ["Blend tofu, cocoa, protein powder and maple until silky.","Chill 15 min."],
 tip="Nobody guesses it's tofu.")
rec("V20","Roasted Chickpeas & Edamame Snack Mix","Snack",25,2,
 [("canned chickpeas, drained",70),("edamame, shelled (frozen)",60),("pumpkin seeds",10),("olive oil",3)],
 ["Dry chickpeas, toss with oil and paprika.","Roast with edamame at 400°F / 200°C for 20 min, add pumpkin seeds last 3 min."])
for r in XR:
    if r["id"].startswith("V") and not r["swap"]: r["swap"] = "Already vegan."

def macros(r):
    k = p = c = f = 0
    for n, g in r["ings"]:
        a = ING[n]; k += a[0]*g/100; p += a[1]*g/100; c += a[2]*g/100; f += a[3]*g/100
    return round(k), round(p), round(c), round(f)
XM = {r["id"]: macros(r) for r in XR}

# Image prompts (overhead/45°, natural light, homemade look, no text, no people)
STYLE = ("Realistic food photograph, homemade look, natural window light, 45-degree angle, "
         "on a light wooden table with a linen napkin, shallow depth of field, appetizing, no text, no hands, no people, horizontal 16:9")
def photo_prompt(r):
    main = ", ".join(n for n, _ in r["ings"][:4])
    return f"{r['name']}. Main ingredients visible: {main}. {STYLE}"
