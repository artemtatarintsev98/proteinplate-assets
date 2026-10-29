# Nutrition per 100 g (approx. USDA FoodData Central values): kcal, protein, carbs, fat
# shop: (store section, unit grams for "1 piece" or None)
ING = {
 # proteins
 "chicken breast":        (120, 22.5, 0, 2.6, "Meat & Fish"),
 "chicken thigh, boneless skinless": (121, 19.7, 0, 4.1, "Meat & Fish"),
 "ground turkey (93% lean)": (150, 18.7, 0, 8.3, "Meat & Fish"),
 "lean ground beef (93%)": (152, 21.0, 0, 7.0, "Meat & Fish"),
 "salmon fillet":         (208, 20.4, 0, 13.4, "Meat & Fish"),
 "cod fillet":            (82, 17.8, 0, 0.7, "Meat & Fish"),
 "shrimp, peeled":        (85, 20.1, 0, 0.5, "Meat & Fish"),
 "canned tuna in water, drained": (116, 25.5, 0, 0.8, "Pantry"),
 "smoked salmon":         (117, 18.3, 0, 4.3, "Meat & Fish"),
 "turkey breast deli slices": (104, 17.1, 4.2, 1.7, "Meat & Fish"),
 "eggs":                  (143, 12.6, 0.7, 9.5, "Dairy & Eggs"),
 "egg whites (carton)":   (52, 10.9, 0.7, 0.2, "Dairy & Eggs"),
 "nonfat Greek yogurt":   (59, 10.3, 3.6, 0.4, "Dairy & Eggs"),
 "low-fat cottage cheese (2%)": (81, 10.5, 4.8, 2.3, "Dairy & Eggs"),
 "part-skim mozzarella":  (254, 24.3, 2.8, 15.9, "Dairy & Eggs"),
 "feta":                  (264, 14.2, 4.1, 21.3, "Dairy & Eggs"),
 "parmesan, grated":      (420, 29.6, 3.2, 28.0, "Dairy & Eggs"),
 "skim milk":             (34, 3.4, 5.0, 0.1, "Dairy & Eggs"),
 "firm tofu":             (144, 17.3, 2.8, 8.7, "Produce"),
 "edamame, shelled (frozen)": (121, 11.9, 8.9, 5.2, "Frozen"),
 # carbs
 "rolled oats":           (379, 13.2, 67.7, 6.5, "Pantry"),
 "whole wheat bread":     (252, 12.4, 43.0, 3.5, "Bakery"),
 "whole wheat tortilla":  (310, 9.0, 50.0, 8.0, "Bakery"),
 "whole wheat pita":      (266, 9.8, 55.0, 2.6, "Bakery"),
 "whole wheat English muffin": (203, 8.8, 40.0, 2.0, "Bakery"),
 "cooked white rice":     (130, 2.7, 28.2, 0.3, "Pantry"),
 "cooked brown rice":     (123, 2.7, 25.6, 1.0, "Pantry"),
 "cooked quinoa":         (120, 4.4, 21.3, 1.9, "Pantry"),
 "whole wheat pasta (dry)": (350, 14.0, 70.0, 2.5, "Pantry"),
 "potatoes":              (77, 2.0, 17.0, 0.1, "Produce"),
 "sweet potato":          (86, 1.6, 20.1, 0.1, "Produce"),
 "canned chickpeas, drained": (139, 7.0, 22.5, 2.6, "Pantry"),
 "canned black beans, drained": (132, 8.9, 23.7, 0.5, "Pantry"),
 "cooked lentils":        (116, 9.0, 20.1, 0.4, "Pantry"),
 "rice cakes":            (387, 8.2, 81.5, 2.8, "Pantry"),
 "frozen corn":           (86, 3.2, 19.0, 1.2, "Frozen"),
 # veg & fruit
 "broccoli":              (34, 2.8, 6.6, 0.4, "Produce"),
 "spinach":               (23, 2.9, 3.6, 0.4, "Produce"),
 "bell pepper":           (31, 1.0, 6.0, 0.3, "Produce"),
 "zucchini":              (17, 1.2, 3.1, 0.3, "Produce"),
 "cherry tomatoes":       (18, 0.9, 3.9, 0.2, "Produce"),
 "cucumber":              (15, 0.7, 3.6, 0.1, "Produce"),
 "red onion":             (40, 1.1, 9.3, 0.1, "Produce"),
 "mixed salad greens":    (20, 1.5, 3.5, 0.3, "Produce"),
 "green beans":           (31, 1.8, 7.0, 0.2, "Produce"),
 "carrots":               (41, 0.9, 9.6, 0.2, "Produce"),
 "mushrooms":             (22, 3.1, 3.3, 0.3, "Produce"),
 "frozen stir-fry vegetables": (40, 2.0, 7.0, 0.3, "Frozen"),
 "avocado":               (160, 2.0, 8.5, 14.7, "Produce"),
 "banana":                (89, 1.1, 22.8, 0.3, "Produce"),
 "frozen mixed berries":  (50, 0.7, 12.0, 0.3, "Frozen"),
 "apple":                 (52, 0.3, 13.8, 0.2, "Produce"),
 "lemon juice":           (22, 0.4, 6.9, 0.2, "Produce"),
 # fats, sauces, extras
 "olive oil":             (884, 0, 0, 100, "Pantry"),
 "peanut butter":         (588, 25.0, 20.0, 50.0, "Pantry"),
 "almonds":               (579, 21.2, 21.6, 49.9, "Pantry"),
 "chia seeds":            (486, 16.5, 42.1, 30.7, "Pantry"),
 "hummus":                (166, 7.9, 14.3, 9.6, "Dairy & Eggs"),
 "salsa":                 (36, 1.5, 7.0, 0.2, "Pantry"),
 "low-sodium soy sauce":  (53, 8.1, 4.9, 0.6, "Pantry"),
 "honey":                 (304, 0.3, 82.4, 0, "Pantry"),
 "marinara sauce":        (50, 1.6, 8.0, 1.5, "Pantry"),
 "cocoa powder (unsweetened)": (228, 19.6, 57.9, 13.7, "Pantry"),
 "garlic":                (149, 6.4, 33.1, 0.5, "Produce"),
 "teriyaki sauce":        (89, 5.9, 15.6, 0.0, "Pantry"),
 "light coconut milk":    (73, 0.7, 2.9, 6.6, "Pantry"),
 "curry paste":           (100, 2.0, 12.0, 5.0, "Pantry"),
 "tzatziki":              (90, 4.0, 4.0, 6.5, "Dairy & Eggs"),
 "dark chocolate chips":  (500, 5.0, 60.0, 30.0, "Pantry"),
 "granola":               (471, 10.0, 64.0, 20.0, "Pantry"),
 "pickled jalapeños / hot sauce": (20, 0.5, 4.0, 0.2, "Pantry"),
}

# Recipe: id, name, meal, minutes, serves, ingredients [(name, grams per serving)], steps, swap (vegetarian)
R = []
def rec(id, name, meal, mins, serves, ings, steps, swap="", tip=""):
    R.append(dict(id=id, name=name, meal=meal, mins=mins, serves=serves, ings=ings, steps=steps, swap=swap, tip=tip))

# ---------------- BREAKFASTS ----------------
rec("B1","Berry Protein Overnight Oats","Breakfast",5,1,
 [("rolled oats",40),("nonfat Greek yogurt",150),("skim milk",100),("frozen mixed berries",80),("chia seeds",8)],
 ["Stir oats, yogurt, milk and chia in a jar.","Top with berries, close and refrigerate overnight (make 3–4 jars on Sunday).","Eat cold, or microwave 60–90 sec."],
 swap="Already vegetarian.", tip="Make 4 jars at once — they keep 4 days.")
rec("B2","Spinach & Feta Egg Muffins + Toast","Breakfast",25,1,
 [("eggs",100),("egg whites (carton)",120),("spinach",30),("bell pepper",40),("feta",15),("whole wheat bread",35)],
 ["Heat oven to 375°F / 190°C. Grease a 12-cup muffin tin.","Whisk eggs and egg whites, add chopped spinach, pepper and feta. Pour into 6 cups (3 per serving).","Bake 18–20 min. Serve 3 muffins with 1 slice of toast."],
 swap="Already vegetarian.", tip="One batch = 4 breakfasts. Reheat 30 sec.")
rec("B3","Cottage Cheese Pancakes","Breakfast",15,1,
 [("low-fat cottage cheese (2%)",120),("eggs",50),("rolled oats",35),("frozen mixed berries",60),("honey",7)],
 ["Blend cottage cheese, egg and oats until smooth.","Cook small pancakes in a non-stick pan, 2 min per side.","Top with warmed berries and a drizzle of honey."],
 swap="Already vegetarian.")
rec("B4","Smoked Salmon Breakfast Muffin","Breakfast",5,1,
 [("whole wheat English muffin",66),("smoked salmon",60),("low-fat cottage cheese (2%)",60),("cucumber",40),("eggs",50)],
 ["Toast the muffin. Fry or boil the egg.","Spread cottage cheese, add egg, salmon and cucumber slices.","Season with black pepper and lemon."],
 swap="Swap salmon for 2 extra egg whites.")
rec("B5","Chocolate Peanut Butter Yogurt Bowl","Breakfast",3,1,
 [("nonfat Greek yogurt",220),("cocoa powder (unsweetened)",6),("peanut butter",12),("banana",60),("granola",15)],
 ["Stir cocoa into yogurt until smooth (add a splash of milk if thick).","Top with sliced banana, peanut butter and granola."],
 swap="Already vegetarian.", tip="Tastes like dessert. Under 5 minutes.")
rec("B6","Turkey & Egg White Breakfast Burrito","Breakfast",12,1,
 [("whole wheat tortilla",45),("egg whites (carton)",150),("turkey breast deli slices",40),("bell pepper",40),("salsa",30),("part-skim mozzarella",15)],
 ["Scramble egg whites with diced pepper in a non-stick pan.","Warm tortilla, add turkey, eggs, cheese and salsa. Roll up.","Optional: wrap 4 in foil and freeze, reheat 2 min."],
 swap="Swap turkey for 60 g black beans.")
rec("B7","Savory Cottage Cheese Toast","Breakfast",5,1,
 [("whole wheat bread",70),("low-fat cottage cheese (2%)",150),("cherry tomatoes",60),("eggs",50)],
 ["Toast 2 slices of bread.","Top with cottage cheese, sliced tomatoes and a soft-boiled egg.","Finish with salt, pepper and chili flakes."],
 swap="Already vegetarian.")
rec("B8","Apple Pie Protein Oats","Breakfast",8,1,
 [("rolled oats",45),("skim milk",200),("egg whites (carton)",100),("apple",80),("almonds",8)],
 ["Simmer oats in milk 3 min.","Whisk in egg whites and stir 1–2 min until fluffy (they disappear into the oats).","Top with diced apple, cinnamon and chopped almonds."],
 swap="Already vegetarian.", tip="The egg-white trick adds 11 g protein you can't taste.")

# ---------------- LUNCHES (meal-prep) ----------------
rec("L1","Greek Chicken Rice Bowls","Lunch",35,4,
 [("chicken breast",150),("cooked brown rice",120),("cucumber",60),("cherry tomatoes",60),("red onion",15),("tzatziki",40),("feta",10),("olive oil",3)],
 ["Toss chicken with oil, lemon, oregano, garlic powder, salt. Bake at 425°F / 220°C for 20–22 min.","Slice and divide into 4 containers with rice and chopped veg.","Add tzatziki and feta in a small container on the side."],
 swap="Swap chicken for 180 g chickpeas + 40 g extra feta.", tip="Keeps 4 days in the fridge.")
rec("L2","Turkey Taco Burrito Bowls","Lunch",25,4,
 [("ground turkey (93% lean)",130),("cooked white rice",100),("canned black beans, drained",60),("frozen corn",40),("salsa",50),("mixed salad greens",30),("nonfat Greek yogurt",30)],
 ["Brown turkey with taco seasoning (cumin, paprika, chili, garlic, salt) 8–10 min.","Warm beans and corn.","Divide rice, turkey, beans, corn into 4 containers. Top with salsa, greens and Greek yogurt (instead of sour cream)."],
 swap="Swap turkey for 150 g crumbled firm tofu.")
rec("L3","Tuna Chickpea Power Salad","Lunch",10,2,
 [("canned tuna in water, drained",110),("canned chickpeas, drained",80),("cucumber",60),("cherry tomatoes",60),("red onion",15),("mixed salad greens",40),("olive oil",7),("lemon juice",15),("feta",10)],
 ["Mix tuna, chickpeas, chopped veg and feta.","Dress with olive oil, lemon, salt, pepper.","Serve over greens. Keeps 2 days."],
 swap="Swap tuna for 2 boiled eggs + 50 g extra chickpeas.")
rec("L4","Teriyaki Salmon Rice Bowls","Lunch",30,4,
 [("salmon fillet",120),("cooked white rice",110),("broccoli",100),("edamame, shelled (frozen)",40),("teriyaki sauce",15)],
 ["Brush salmon with teriyaki, bake at 400°F / 200°C for 12–14 min.","Steam broccoli and edamame.","Divide into containers with rice, drizzle remaining teriyaki."],
 swap="Swap salmon for 150 g firm tofu, baked the same way.")
rec("L5","Chicken Pesto-Free Pasta Salad","Lunch",25,4,
 [("chicken breast",120),("whole wheat pasta (dry)",55),("cherry tomatoes",60),("spinach",30),("part-skim mozzarella",20),("olive oil",5),("lemon juice",10)],
 ["Cook pasta, rinse under cold water.","Bake or pan-cook seasoned chicken, slice.","Toss everything with oil, lemon, basil, salt. Divide into 4 boxes."],
 swap="Swap chicken for 120 g white beans + 15 g parmesan.")
rec("L6","Egg Roll in a Bowl","Lunch",20,4,
 [("lean ground beef (93%)",120),("frozen stir-fry vegetables",150),("carrots",40),("cooked white rice",100),("low-sodium soy sauce",15),("garlic",4)],
 ["Brown beef with garlic 6–7 min.","Add stir-fry veg and grated carrot, cook 5 min.","Season with soy sauce and ginger. Divide over rice."],
 swap="Swap beef for 150 g firm tofu or 120 g edamame.")
rec("L7","Mediterranean Chicken Wraps","Lunch",10,1,
 [("whole wheat tortilla",45),("chicken breast",120),("hummus",30),("mixed salad greens",30),("cucumber",50),("cherry tomatoes",40),("feta",10)],
 ["Use pre-cooked chicken from Sunday prep (or rotisserie breast, skin removed).","Spread hummus on tortilla, add chicken, veg and feta.","Roll tightly, cut in half."],
 swap="Swap chicken for 120 g firm tofu + extra hummus.")
rec("L8","Lentil & Turkey Chili","Lunch",35,4,
 [("ground turkey (93% lean)",100),("cooked lentils",100),("canned black beans, drained",50),("marinara sauce",100),("bell pepper",50),("red onion",30),("nonfat Greek yogurt",30)],
 ["Brown turkey and onion 6 min.","Add pepper, lentils, beans, marinara, chili powder, cumin. Simmer 20 min.","Portion into 4 containers. Top with Greek yogurt."],
 swap="Skip turkey, double the lentils.", tip="Freezes perfectly for 3 months.")

# ---------------- DINNERS ----------------
rec("D1","Sheet-Pan Lemon Garlic Chicken & Potatoes","Dinner",35,2,
 [("chicken breast",160),("potatoes",180),("green beans",120),("olive oil",8),("garlic",5),("lemon juice",10)],
 ["Heat oven to 425°F / 220°C. Cube potatoes, toss with half the oil, roast 10 min.","Add chicken and green beans, toss with remaining oil, garlic, lemon, herbs.","Roast 20 more minutes until chicken hits 165°F / 74°C."],
 swap="Swap chicken for 200 g chickpeas (roast them crispy).")
rec("D2","15-Minute Shrimp Stir-Fry","Dinner",15,2,
 [("shrimp, peeled",170),("frozen stir-fry vegetables",200),("cooked white rice",130),("low-sodium soy sauce",15),("garlic",5),("olive oil",5),("honey",5)],
 ["Heat oil, cook garlic 30 sec, add shrimp 2 min per side. Remove.","Stir-fry vegetables 4–5 min.","Add shrimp back with soy, honey and a splash of water. Serve over rice."],
 swap="Swap shrimp for 200 g firm tofu cubes.")
rec("D3","Turkey Meatballs in Marinara + Zucchini Pasta","Dinner",30,3,
 [("ground turkey (93% lean)",150),("eggs",15),("parmesan, grated",8),("marinara sauce",120),("zucchini",150),("whole wheat pasta (dry)",40)],
 ["Mix turkey, egg, parmesan, garlic powder, salt. Roll 12 meatballs.","Bake at 400°F / 200°C for 15 min, then simmer in marinara 5 min.","Serve over half pasta / half spiralized zucchini."],
 swap="Use store-bought veggie meatballs (check ≥15 g protein per serving).")
rec("D4","Baked Salmon, Sweet Potato & Broccoli","Dinner",30,2,
 [("salmon fillet",140),("sweet potato",180),("broccoli",150),("olive oil",4)],
 ["Cube sweet potato, roast at 425°F / 220°C for 15 min.","Add salmon (salt, paprika, lemon) and broccoli with oil to the tray.","Roast 12 more minutes."],
 swap="Swap salmon for 200 g firm tofu.")
rec("D5","Beef & Broccoli","Dinner",20,3,
 [("lean ground beef (93%)",140),("broccoli",180),("cooked brown rice",120),("low-sodium soy sauce",15),("garlic",5),("honey",5)],
 ["Brown beef with garlic, break into pieces.","Add broccoli and 3 tbsp water, cover 4 min.","Stir in soy and honey. Serve over rice."],
 swap="Swap beef for 140 g edamame + 100 g tofu.")
rec("D6","Chicken Fajita Bowls","Dinner",25,2,
 [("chicken breast",160),("bell pepper",150),("red onion",60),("cooked white rice",100),("salsa",40),("avocado",30),("olive oil",5)],
 ["Slice chicken and veg into strips, toss with fajita spices and oil.","Cook in a hot pan 8–10 min (or sheet pan 20 min at 425°F / 220°C).","Serve over rice with salsa and avocado."],
 swap="Swap chicken for 180 g black beans + 100 g tofu.")
rec("D7","Crispy Cod Tacos","Dinner",20,2,
 [("cod fillet",180),("whole wheat tortilla",70),("mixed salad greens",40),("nonfat Greek yogurt",40),("lemon juice",10),("cherry tomatoes",60),("olive oil",4)],
 ["Season cod with paprika, garlic, salt. Pan-sear in oil 3–4 min per side.","Mix yogurt with lemon and pinch of salt for a quick sauce.","Fill tortillas with cod, greens, tomatoes and sauce."],
 swap="Swap cod for 200 g firm tofu or 2 eggs + beans.")
rec("D8","Chicken Thigh Curry (Lightened)","Dinner",30,4,
 [("chicken thigh, boneless skinless",160),("light coconut milk",60),("curry paste",12),("spinach",60),("red onion",40),("cooked white rice",110)],
 ["Brown sliced chicken with onion 6 min.","Stir in curry paste, then coconut milk and 1/2 cup water. Simmer 12 min.","Wilt in spinach. Serve over rice."],
 swap="Swap chicken for chickpeas + tofu.")
rec("D9","Loaded Turkey Stuffed Peppers","Dinner",40,4,
 [("ground turkey (93% lean)",130),("bell pepper",180),("cooked white rice",60),("canned black beans, drained",40),("salsa",50),("part-skim mozzarella",20)],
 ["Halve peppers, remove seeds.","Brown turkey with taco spices, mix with rice, beans, salsa.","Fill peppers, top with cheese, bake at 375°F / 190°C for 25 min."],
 swap="Swap turkey for lentils.")
rec("D10","Garlic Shrimp & Spinach Pasta","Dinner",20,2,
 [("shrimp, peeled",150),("whole wheat pasta (dry)",60),("spinach",80),("garlic",6),("olive oil",6),("parmesan, grated",8),("lemon juice",10)],
 ["Cook pasta. Save 1/2 cup pasta water.","Sauté garlic in oil, add shrimp 2 min per side, add spinach to wilt.","Toss with pasta, lemon, parmesan and a splash of pasta water."],
 swap="Swap shrimp for 120 g white beans + 1 egg.")
rec("D11","Tofu & Veggie Peanut Noodles","Dinner",20,2,
 [("firm tofu",180),("whole wheat pasta (dry)",50),("frozen stir-fry vegetables",150),("peanut butter",10),("low-sodium soy sauce",15),("edamame, shelled (frozen)",40)],
 ["Press and cube tofu, pan-fry until golden (8 min).","Cook noodles/pasta; heat vegetables and edamame.","Whisk peanut butter, soy, lime and hot water into a sauce, toss everything."],
 swap="Already vegetarian.", tip="Your weekly meat-free night.")
rec("D12","Burger Night Lettuce-Optional Bowls","Dinner",20,2,
 [("lean ground beef (93%)",140),("potatoes",150),("cherry tomatoes",60),("mixed salad greens",50),("pickled jalapeños / hot sauce",20),("part-skim mozzarella",15),("olive oil",4)],
 ["Cut potatoes into wedges, toss with oil, air-fry or bake at 425°F / 220°C for 22 min.","Form 1 patty per person, cook 4 min per side.","Bowl: greens, tomatoes, chopped burger, cheese, wedges, pickles/hot sauce."],
 swap="Use a veggie burger with ≥18 g protein.")
rec("D13","One-Pan Chicken Fried Rice","Dinner",20,3,
 [("chicken breast",130),("cooked white rice",130),("eggs",50),("frozen stir-fry vegetables",120),("low-sodium soy sauce",15),("olive oil",4)],
 ["Use day-old rice. Cook diced chicken in oil 6 min, push aside.","Scramble eggs, add vegetables and rice.","Stir-fry with soy sauce 3–4 min until hot."],
 swap="Swap chicken for tofu.")
rec("D14","Baked Feta Chicken & Cherry Tomatoes","Dinner",30,2,
 [("chicken breast",160),("cherry tomatoes",150),("feta",25),("zucchini",120),("cooked quinoa",100),("olive oil",5)],
 ["Put tomatoes, sliced zucchini and feta block in a dish, add chicken, oil, oregano.","Bake at 400°F / 200°C for 25 min.","Smash tomatoes and feta into a sauce, serve over quinoa."],
 swap="Swap chicken for 200 g chickpeas.")
rec("D15","Turkey Smash Tacos","Dinner",15,2,
 [("ground turkey (93% lean)",150),("whole wheat tortilla",70),("part-skim mozzarella",15),("mixed salad greens",40),("salsa",40),("nonfat Greek yogurt",30)],
 ["Season turkey with taco spices. Press a thin layer onto each tortilla.","Cook meat-side down in a hot pan 3 min, flip 1 min.","Top with cheese, greens, salsa and yogurt."],
 swap="Use crumbled tofu with taco spices.", tip="The viral recipe — lighter.")
rec("D16","Cod with Lemon Herb Quinoa & Green Beans","Dinner",25,2,
 [("cod fillet",200),("cooked quinoa",130),("green beans",150),("olive oil",8),("lemon juice",15)],
 ["Bake cod with oil, lemon, garlic, parsley at 400°F / 200°C for 12–15 min.","Steam green beans 5 min.","Toss quinoa with lemon and herbs. Plate everything."],
 swap="Swap cod for 200 g tofu.")

# ---------------- SNACKS ----------------
rec("S1","Greek Yogurt Berry Cup","Snack",2,1,
 [("nonfat Greek yogurt",170),("frozen mixed berries",60),("honey",5)],
 ["Top yogurt with berries and honey."], swap="Already vegetarian.")
rec("S2","Cottage Cheese & Apple Crunch","Snack",3,1,
 [("low-fat cottage cheese (2%)",150),("apple",80),("almonds",8)],
 ["Slice apple, eat with cottage cheese and almonds. Cinnamon on top."], swap="Already vegetarian.")
rec("S3","Hard-Boiled Eggs & Veggies","Snack",2,1,
 [("eggs",100),("carrots",60),("cucumber",60),("hummus",20)],
 ["Boil a dozen eggs on Sunday (10 min, ice bath).","Pack 2 eggs with veg sticks and hummus."], swap="Already vegetarian.")
rec("S4","Tuna Rice Cakes","Snack",3,1,
 [("canned tuna in water, drained",70),("rice cakes",18),("nonfat Greek yogurt",20),("cucumber",30)],
 ["Mix tuna with yogurt, lemon, pepper.","Spread on 2 rice cakes, top with cucumber."], swap="Use mashed white beans + egg.")
rec("S5","Edamame with Sea Salt","Snack",5,1,
 [("edamame, shelled (frozen)",120)],
 ["Microwave edamame 3 min, sprinkle with salt and chili."], swap="Already vegetarian.")
rec("S6","Turkey & Cheese Roll-Ups","Snack",2,1,
 [("turkey breast deli slices",70),("part-skim mozzarella",20),("cucumber",50)],
 ["Roll turkey around cheese sticks and cucumber spears."], swap="Swap for S2 or S5.")
rec("S7","Chocolate Protein Pudding","Snack",3,1,
 [("nonfat Greek yogurt",170),("cocoa powder (unsweetened)",6),("dark chocolate chips",6),("honey",5)],
 ["Stir cocoa and honey into yogurt, top with chips. Chill 10 min."], swap="Already vegetarian.", tip="Kills the evening sweet craving.")
rec("S8","Peanut Butter Banana Yogurt","Snack",3,1,
 [("nonfat Greek yogurt",150),("banana",50),("peanut butter",8)],
 ["Top yogurt with banana slices and a drizzle of peanut butter."], swap="Already vegetarian.")

# ---------------- WEEK PLANS ----------------
# each day: (breakfast, lunch, dinner, snack)
DAYS = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
WEEKS = [
 {"title":"Week 1 · Build the Habit","theme":"Simple wins. Same breakfast most days, two prepped lunches, easy dinners.",
  "plan":[("B1","L1","D1","S1"),("B1","L1","D1","S3"),("B2","L1","D2","S1"),("B2","L1","D3","S3"),("B1","L2","D3","S7"),("B2","L2","D4","S1"),("B5","L2","D6","S3")]},
 {"title":"Week 2 · Find Your Rhythm","theme":"New flavors, same structure. You already know the routine.",
  "plan":[("B3","L3","D5","S2"),("B6","L3","D5","S5"),("B3","L4","D8","S2"),("B6","L4","D8","S7"),("B3","L4","D7","S5"),("B6","L4","D11","S2"),("B7","L4","D12","S8")]},
 {"title":"Week 3 · Level Up","theme":"Fewer decisions, more protein, still 20 minutes or less most nights.",
  "plan":[("B8","L5","D9","S4"),("B4","L5","D9","S1"),("B8","L5","D10","S6"),("B4","L5","D13","S4"),("B8","L6","D13","S1"),("B4","L6","D14","S6"),("B5","L6","D15","S7")]},
 {"title":"Week 4 · Make It Yours","theme":"Your favorites from weeks 1–3 plus a few new ones. This is the routine you keep.",
  "plan":[("B1","L8","D16","S8"),("B7","L8","D16","S3"),("B1","L8","D6","S2"),("B7","L8","D2","S8"),("B1","L7","D11","S5"),("B3","L7","D15","S7"),("B5","L7","D4","S1")]},
]
