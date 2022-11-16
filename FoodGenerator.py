import os
from tkinter import *
from tkinter import ttk
import webbrowser
import random
def aboutme():
    aboutmewin = Tk() 
    aboutmewin.resizable(False, False)      
    aboutmewin.title("About The App!")
    aboutMeTitle = Label(aboutmewin,font=("Consolas", 40), text="About The App!",bg="#FFD3AF").pack()
    aboutmewin.config(bg="#FFD3AF")
    aboutmedesc = Label(aboutmewin, font=("Consolas", 15), text="This app will help you filter recipes for meals you can and can’t eat.\n All you have to do is input your allergies into the app and BOOM, \nit loads the meals you can eat.",bg="#FFD3AF").pack()
    creditss = Label(aboutmewin,font=("Consolas", 40), text="Credits",bg="#FFD3AF").pack()
    creditsdesc = Label(aboutmewin, font=("Consolas", 15), text="-Thawin Chalermdit: Coding, Graphic Design, First Tester. from DSIL School",bg="#FFD3AF").pack()
    close = Button(aboutmewin,font=("Consolas",20),bg=random.choice(["yellow","#C0FFB0"]), text="Close!", command=aboutmewin.destroy).pack()
def start():
    try:
        welcome.destroy()
    except:
        pass

    foodAndIngredients = {"pineapple pizza":["pineapple", "pizza", "ham", "cheese", "mozzarella", "tomato sauce", "pizza dough", "wheat", "milk"]
        ,"burger":["ground beef","wheat","tomato",'cheese', "garlic", "egg", "onion", "black pepper", "bread crumbs"]
        ,"steak with butter":["beef", "sauce", "butter", "black pepper", "onion", "minced garlic", "milk"]
        ,"steak":["beef", "sauce", "black pepper", "onion", "minced garlic"]
        , "milky mashed potatos":["herbs", "potato", "milk", "butter", "garlic", "russet potato", "black pepper", "cream", "salt"]
        , "mashed potatos":["herbs", "potato", "garlic", "salt"]
        ,"bread": ["wheat", "salt", "leavening agent", "milk", "meal"]
        , "yolk": ["yolk"]
        , "normal lays": ["potato", "vegatable oil", "salt"]
        , "egg tofu": ["soy", "egg", "soy milk"]
        , "tofu": ["soy", "soy milk"]
        , "ommlet": ["egg", "butter"]
        , "McDonalds French Fries":["potato", "salt", "vegetable oil", "soybean oil"]
        , "McDonalds Nuggets":["white boneless chicken", "chicken", "water", "vegatable oil", "wheat", "flour","vegatable starch"]
        , "Turkey with Butter":["salt", "pepper", "lemon", "garlic", "onion", "thyme", "milk"]
        ,"Butterball Turkey":["salt", "pepper", "lemon", "garlic", "onion", "thyme", "water"]
        ,"Bacon":["salt", "spices", "pork"]
        ,"Apple":["fruit"]
        , "Sushi":["rice", "cucumber", "nori", "avocado", "fish", "vegatables", "sugar", "salt", "rice vinegar", "kelp"]
        ,"Pudding":["wheat", "rice", "egg", "bread","corn", "milk"]
        ,"brocoli":["vegatable"]
        ,"Cookies":["wheat", "egg", "sugar", "oil", "fat", "milk", "butter", "chocolate chips"]
        ,"Strawberry Ice Cream":["milk", "cream", "butterfat", "sugar", "strawberry", "egg"]
        ,"Chocolate Ice Cream":["milk", "cream", "butterfat", "sugar", "chocolate", "egg"]
        ,"Vanilla Ice Cream":["milk", "cream", "butterfat", "sugar", "strawberry", "vanilla", "fruit", "orchids", "egg"]
        ,"Sweet Potato":["vegetable"]
        ,"Strawberry":["fruit"]
        ,"biscuits":["wheat", "salt", "butter", "milk", "vegetable", "baking powder"]
        ,"ham":["pork"]
        ,"shrimps":["water","proteins"]
        ,"Calzone":["milk","pizza", "ham", "cheese", "mozzarella", "tomato sauce", "pizza dough", "wheat","pepperoni", "egg", "garlic", "sausage", "salt", "parmesan", "lamb"]
        ,"Chocolate Cake":["milk", "chocolate","cream", "egg", "butter", "wheat", "flour", "cocoa powder", "vanilla", "fruit", "orchids", "baking powder", "sugar"]
        ,"Tomato":["vegetable"]
        ,"orange":["fruit"]
        ,"Donut":["wheat", "egg","milk", "oil", "salt", "leavening agent", "milk", "meal"]
        ,"Taco":["beef", "pork", "chicken", "fish", "beans", "vegetables", "cheese", "milk","onion","chiles", "wheat"]
        ,"pizza":["cheese", "milk", "wheat", "pizza dough", "sauce","flour","tomato", "mozzarella", "basil"]
        ,"mango":["fruit"]
        ,"fried chicken":["chicken", "frying", "egg", "wheat", "flour", "vegetable", "garlic", " buttermilk", "milk", "black pepper"]
        ,"cake":["flour", "wheat", "egg", "butter", "milk", "oil", "baking soda", "leavening agent"]
        ,"Meatballs":["meat", "beef", "cheese", "milk", "tomato", "egg", "wheat", "salt", "leavening agent", "milk", "meal", "bread", "onion", "garlic", "bread crumbs"]
        ,"Corn":["vegetable"]
        ,"Salmon":["water", "protein", "fish"]
        ,"Baked Sweet Potatoes":["black beans", "corn", "radish", "red onion", "cilantro"]
        ,"Grain Bowls":["rice", "farro", "quinoa", "millet", "wheat"]
        ,"Crispy Microwaved Bacon":["bacon"]
        ,"Bacon Mac and Cheese":["bacon", "wheat", "milk", "water", "mac", "cheese","egg", "wheat", "water", "rice"]
        ,"Pasta":["egg", "wheat", "water", "rice"]
        }
    def check_allergens():
        allergens = []
        if wheatCheck.get() == 1: allergens.append("wheat")
        if milkCheck.get() == 1: allergens.append("milk")
        if fishCheck.get() == 1: allergens.append("fish")
        if eggCheck.get() == 1: allergens.append("egg")
        if peanutCheck.get() == 1: allergens.append("peanut")
        if soyCheck.get() == 1: allergens.append("soy")
        if treeNutCheck.get() == 1: allergens.append("treeNut")
        if sesameCheck.get() == 1: allergens.append("sesame")
        if shellFishCheck.get() == 1: allergens.append("shellFish")
        return allergens
    def checkFoodThatCanEat():
        def goBackRightNow():
            windowCheckFood.destroy()
            start()
        allergens = check_allergens()
        window.destroy()
        windowCheckFood = Tk()
        windowCheckFood.resizable(False, False)
        windowCheckFood.title("Food Generator For People With Allergies: Check Foods You can Eat!")
        windowCheckFood.geometry("800x600")
        windowCheckFood.config(bg="#FFD3AF")

        scrollbar = Scrollbar(windowCheckFood)
        scrollbar.pack( side = RIGHT,
                fill = Y )
        
        mylist = Listbox(windowCheckFood, yscrollcommand=scrollbar.set , font=("Consolas", 15), bg="#DEFF96")
        def selected_item():
            try:
                for i in mylist.curselection():
                    
                    if not "can't" in mylist.get(i):
                        got = mylist.get(i)[12:]
                    else:
                        got = mylist.get(i)[14:str(mylist.get(i)).index("because")-1]
                    webbrowser.open(f"https://www.google.com/search?q={got}") if got != "" else print()                
            except Exception:
                pass
        def ingredient_item():
            try:
                for i in mylist.curselection():
                    
                    if not "can't" in mylist.get(i):
                        got = mylist.get(i)[12:]
                    else:
                        got = mylist.get(i)[14:str(mylist.get(i)).index("because")-1]
                    ingredientFood = Tk()  
                    ingredientFood.resizable(False, False)     
                    ingredientFood.title(got)
                    ingredientFood.config(bg="#FFD3AF")
                    foodTitle = Label(ingredientFood,font=("Consolas", 30), text=got, bg="#FFD3AF").pack()
                    ingredientLabel = Label(ingredientFood, font=("Consolas",20),bg="#FFD3AF", text="Ingredients: ").pack()
                    ingredients = Label(ingredientFood, font=("Consolas",20),bg="#FFD3AF", text=", ".join(foods[got])).pack()
                    close = Button(ingredientFood,font=("Consolas",20),bg="#DEFF96", text="Close!", command=ingredientFood.destroy).pack()
            except Exception:
                pass
        allergenFontSize = 20
        if len(allergens) > 5 and len(allergens) < 7:
            allergenFontSize = 15
        elif len(allergens) > 7 and len(allergens) < 10:
            allergenFontSize = 13
        else:
            allergenFontSize = 20
        AllergenLabel = Label(windowCheckFood, text=f"Allergies: {', '.join(allergens)}" if allergens != [] else "Allergens: None!",
                font=("Consolas", allergenFontSize),bg="#FFD3AF")
        AllergenLabel.pack()
        red = Label(windowCheckFood, font=("Consolas",20),bg="#FFD3AF", fg="red", text="Red Text = You cannot eat this.").pack()
        green = Label(windowCheckFood, font=("Consolas",20),bg="#FFD3AF", fg="green", text="Red Text = You can eat this.").pack()
        goBack = Button(windowCheckFood, font=("Consolas",20),bg="yellow", text="Go Back",command=goBackRightNow).pack()
        filterText = Label(windowCheckFood, font=("Consolas",20),bg="#FFD3AF", text="Filter Search...").pack()
        filterInput = Entry(windowCheckFood, font=("Consolas",20))
        filterInput.pack()
        allergies = allergens
        foods = foodAndIngredients
        resultCanEat = []
        def update(data):
            mylist.delete(0,END)
            for x, y in data.items():
                allergic = False
                for i in y:
                    if i in allergies:
                        allergic = True
                        break

                if allergic == True:
                    mylist.insert(END, f"You can't eat {x} because it contains {i}.")
                    mylist.itemconfig(END, {'fg': 'red'})
                else:
                    
                    mylist.insert(0, f"You can eat {x}")
                    mylist.itemconfig(0, {'fg': 'green'})
        
        def check(e):
            typed = filterInput.get()
            if typed == "":
                data = foods
            else:
                data = {}
                for item, ingredients in foods.items():
                    if typed.lower() in item.lower():
                        data.update({item:ingredients})
            update(data)
        update(foods)

        
        
            
        
        mylist.pack( fill = BOTH )
        scrollbar.config(command=mylist.yview)
        getSelected = Button(windowCheckFood, font=("Consolas",20),bg="yellow", text="Search!",command=selected_item).pack()
        checkIngredients = Button(windowCheckFood, font=("Consolas",20),bg="yellow", text="Check Ingredients",command=ingredient_item).pack()
        filterInput.bind("<KeyRelease>", check)
        windowCheckFood.mainloop()
    window = Tk()
    window.geometry("800x600")
    window.resizable(False, False)
    window.title("Food Generator For People With Allergies: What are you allergic to?")
    bg = PhotoImage(file="./images/background.png")
    myBackground = Label(window, image=bg).pack()
    wheatCheck = IntVar()
    milkCheck = IntVar()
    fishCheck = IntVar()
    eggCheck = IntVar()
    peanutCheck = IntVar()
    soyCheck = IntVar()
    treeNutCheck = IntVar()
    sesameCheck = IntVar()
    shellFishCheck = IntVar()
    title = Label(window, text="What are you allergic to?",
                font=("Consolas",20),bg="#FFD3AF").place(x=0, y=0)
    wheatCheckbox = Checkbutton(window, variable=wheatCheck, onvalue=1, offvalue=0,bg="#FFD3AF")
    wheatCheckbox.place(x=0, y=50)
    wheatLabel = Label(window, text="Wheat", font=(
        "Consolas", 20),bg="#FFD3AF").place(x=30, y=39)
    MilkCheckBox = Checkbutton(window,variable=milkCheck, onvalue=1, offvalue=0,bg="#FFD3AF").place(x=0, y=100)
    MilkLabel = Label(window, text="Milk", font=(
        "Consolas", 20),bg="#FFD3AF").place(x=30, y=89)
    FishCheckBox = Checkbutton(window,variable=fishCheck, onvalue=1, offvalue=0,bg="#FFD3AF").place(x=0, y=150)
    FishLabel = Label(window, text="Fish", font=(
        "Consolas", 20),bg="#FFD3AF").place(x=30, y=139)
    EggCheckBox = Checkbutton(window,variable=eggCheck, onvalue=1, offvalue=0,bg="#FFD3AF").place(x=0, y=200)
    EggLabel = Label(window, text="Egg", font=(
        "Consolas", 20),bg="#FFD3AF").place(x=30, y=189)
    peanutCheckBox = Checkbutton(window,variable=peanutCheck, onvalue=1, offvalue=0,bg="#FFD3AF").place(x=0, y=250)
    peanutLabel = Label(window, text="Peanut", font=(
        "Consolas", 20),bg="#FFD3AF").place(x=30, y=239)
    soyCheckBox = Checkbutton(window,variable=soyCheck, onvalue=1, offvalue=0,bg="#FFD3AF").place(x=0, y=300)
    soyLabel = Label(window, text="Soy", font=(
        "Consolas", 20),bg="#FFD3AF").place(x=30, y=289)
    treeNutCheckBox = Checkbutton(window,variable=treeNutCheck, onvalue=1, offvalue=0,bg="#FFD3AF").place(x=0, y=350)
    treeNutLabel = Label(window, text="Tree Nuts", font=(
        "Consolas", 20),bg="#FFD3AF").place(x=30, y=339)
    seasameCheckBox = Checkbutton(window,variable=sesameCheck, onvalue=1, offvalue=0,bg="#FFD3AF").place(x=0, y=400)
    seasameLabel = Label(window, text="Sesame", font=(
        "Consolas", 20),bg="#FFD3AF").place(x=30, y=389)
    shellfishCheckBox = Checkbutton(window,variable=shellFishCheck, onvalue=1, offvalue=0,bg="#FFD3AF").place(x=0, y=450)
    shellfishLabel = Label(window, text="Shellfish", font=(
        "Consolas", 20),bg="#FFD3AF").place(x=30, y=439)

    submitButton = Button(window, font=("Consolas",20),bg="#C0FFB0", text="Submit Allergens",command=checkFoodThatCanEat)
    submitButton.place(x=0, y=489)

    window.mainloop()

 
welcome = Tk()
welcome.resizable(False, False)
welcome.title("Welcome To Food Generator!")
welcome.config(bg="#FFD3AF")
title = Label(welcome, text="Welcome To Food Generator", font=("Consolas", 50),bg="#FFD3AF").pack()
title2 = Label(welcome, text="For People With Allergies!", font=("Consolas", 40),bg="#FFD3AF").pack()
randomText = Label(welcome, text=f'Random Sentence for You: {random.choice(["Making some meals...", "I hear you cooking pie :)","You found the legendary food!", "I just filtered a few meals!", "Hope I make a good cake :D"])}', font=("Consolas",20),bg="#FFD3AF").pack()
startTheApp = Button(welcome, text=random.choice(["Let's Go!", "Start!"]), font=("Consolas",20),bg="#C0FFB0", command=start).pack()
aboutMe = Button(welcome, text="About This App", font=("Consolas",20),bg="#C0FFB0", command=aboutme).pack()
welcome.mainloop()