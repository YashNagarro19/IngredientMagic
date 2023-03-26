import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a req.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
            ingredientsList1 = ingredientsList()
            response  = businessLogicTextConversion(req_body,ingredientsList1)
        except Exception as ex:
            return (str) (ex) + "error"
        return func.HttpResponse( response, status_code=200,mimetype='application/json', headers={"Content-Type": "application/json"})

def businessLogicTextConversion(requestBody,ingredientsList):

    try:
        aDict = requestBody.get('ingredients')
        avoidItemsList = []
        ratingList = []
        for item in aDict:
            if item in ingredientsList.keys():
                itemRating= (float) (ingredientsList.get(item))
                if itemRating<2.50:
                    avoidItemsList.append(item)
                ratingList.append(itemRating)

        avoidItems = ', '.join(avoidItemsList)
        avgRating = (str) (round((sum(ratingList)/len(ratingList)),2))

        resp_dict = createResponse(avgRating,avoidItems)
        responseJson = json.dumps(resp_dict, indent=4)
    except Exception as ex:
        responseJson =json.dumps("Some of these ingredients are not present in list. Please try sometime. Error: " + (str)(ex))
        
    return responseJson
     
def createResponse(avgRating,avoidItems):
    responseDict = {"rating": ((str)(avgRating))+" out of 5" , "avoid": avoidItems}
    return responseDict

def ingredientsList():
    ingredientsList = {
    "Spinach": "4.9",
    "Kale": "4.8",
    "Swiss chard": "4.8",
    "Blueberries": "4.4",
    "Blackberries": "4.3",
    "Salmon": "4.2",
    "Oysters": "4.2",
    "Quinoa": "4.0",
    "Greek Yogurt": "3.9",
    "Cottage Cheese": "3.9",
    "Sweet Potatoes": "3.8",
    "Butternut Squash": "3.8",
    "Almonds": "3.7",
    "Pistachios": "3.7",
    "Brazil Nuts": "3.6",
    "Broccoli": "3.6",
    "Brussels Sprouts": "3.5",
    "Lentils": "3.5",
    "Chickpeas": "3.5",
    "Tomatoes": "3.4",
    "Red Bell Peppers": "3.4",
    "Carrots": "3.4",
    "Cantaloupe": "3.4",
    "Grapefruit": "3.4",
    "Oranges": "3.4",
    "Apples": "3.3",
    "Pears": "3.3",
    "Brown Rice": "3.2",
    "Barley": "3.2",
    "Whole Wheat Bread": "3.2",
    "Tuna": "3.1",
    "Turkey Breast": "3.1",
    "Eggs": "3.1",
    "Pumpkin Seeds": "3.1",
    "Sunflower Seeds": "3.0",
    "Edamame": "3.0",
    "Zucchini": "3.0",
    "Green Beans": "3.0",
    "Cucumber": "3.0",
    "Avocado": "2.9",
    "Coconut": "2.9",
    "Dark Chocolate": "2.8",
    "Pecans": "2.8",
    "Flaxseeds": "2.8",
    "Chia Seeds": "2.7",
    "Peanut Butter": "2.7",
    "Tofu": "2.7",
    "Sardines": "2.6",
    "Mackerel": "2.6",
    "Anchovies": "2.6",
    "Brown Lentils": "2.6",
    "Black Beans": "2.6",
    "Red Kidney Beans": "2.6",
    "Chickpea Pasta": "2.6",
    "Spelt": "2.6",
    "Rye": "2.5",
    "Cabbage": "2.5",
    "Cauliflower": "2.5",
    "Beets": "2.5",
    "Garlic": "2.5",
    "Ginger": "2.5",
    "Turmeric": "2.5",
    "Cinnamon": "2.5",
    "Black Pepper": "2.5",
    "Asparagus": "2.4",
    "Mushrooms": "2.4",
    "Onions": "2.4",
    "Leeks": "2.4",
    "Scallions": "2.4",
    "Radishes": "2.3",
    "Artichokes": "2.3",
    "Watercress": "2.3",
    "Arugula": "2.3",
    "Mustard Greens": "2.3",
    "Bok Choy": "2.3",
    "Snow Peas": "2.3",
    "Peppers": "2.3",
    "Jalapeños": "2.3",
    "Habaneros": "2.3",
    "Banana Peppers": "2.3",
    "Acorn Squash": "2.3",
    "Delicata Squash": "2.3",
    "Spaghetti Squash": "2.3",
    "Radicchio": "2.3",
    "Endive": "2.3",
    "Fennel": "2.2",
    "Celery": "2.2",
    "Kohlrabi": "2.2",
    "Turnips": "2.2",
    "Parsnips": "2.2",
    "Rutabagas": "2.2",
    "Sweet Corn": "2.1",
    "Peas": "2.1",
    "Green Peas": "2.1",
    "Snap Peas": "2.1",
    "Lima Beans": "2.1",
    "Pinto Beans": "2.1",
    "Adzuki Beans": "2.1",
    "Kidney Beans": "2.1",
    "Navy Beans": "2.1",
    "Mung Beans": "2.1",
    "Sprouted Beans": "2.1",
    "Sprouted Lentils": "2.1",
    "Sprouted Chickpeas": "2.1",
    "Sprouted Adzuki Beans": "2.1",
    "Sprouted Mung Beans": "2.1",
    "Sprouted Navy Beans": "2.1",
    "Sprouted Pinto Beans": "2.1",
    "Tempeh": "2.1",
    "Seitan": "2.1",
    "Nutritional Yeast": "2.0",
    "Miso": "2.0",
    "Sauerkraut": "2.0",
    "Kimchi": "2.0",
    "Kombucha": "2.0",
    "Kefir": "2.0",
    "Muesli": "2.0",
    "Granola": "2.0",
    "Oatmeal": "2.0",
    "Steel Cut Oats": "2.0",
    "Rolled Oats": "2.0",
    "Amaranth": "2.0",
    "Hemp Seeds": "2.0",
    "Sesame Seeds": "2.0",
    "Walnuts": "2.0",
    "Cashews": "2.0",
    "Hazelnuts": "2.0",
    "Macadamia Nuts": "2.0",
    "Almond Butter": "2.0",
    "Cashew Butter": "2.0",
    "Tahini": "2.0",
    "Hummus": "2.0",
    "Olives": "2.0",
    "Olive Oil": "2.0",
    "Coconut Oil": "2.0",
    "Flaxseed Oil": "2.0",
    "Chia Seed Oil": "2.0",
    "Hemp Seed Oil": "2.0",
    "Sunflower Oil": "2.0",
    "Pumpkin Seed Oil": "2.0",
    "Sesame Oil": "2.0",
    "Safflower Oil": "2.0",
    "Mustard Oil": "2.0",
    "Grapeseed Oil": "2.0",
    "Apple Cider Vinegar": "2.0",
    "Balsamic Vinegar": "2.0",
    "Red Wine Vinegar": "2.0",
    "White Wine Vinegar": "2.0",
    "Nutmeg and Cardamom)}": "1.3",
    "Noodle powder (Wheat flour": "1.6",
    "Edible vegetable oil": "1.3",
    "Wheat flour": "3.5",
    "Salt": "3.5",
    "Wheat gluten": "3.5",
    "Mineral (170(i)) and Guar gum. Masala TASTEMAKER®: Hydrolysed groundnut protein": "3.5",
    "Mixed spices {(24.9%) of which (Onion powder": "2.1",
    "Chilli powder": "3.5",
    "Garlic powder": "3.5",
    "Coriander": "3.5",
    "Turmeric": "3.5",
    "Cumin": "3.5",
    "Aniseed": "3.5",
    "Black pepper": "3.5",
    "Fenugreek": "3.5",
    "Ginger": "4.5",
    "Clove": "3.5",
    "Nutmeg and Cardamom)}": "3.5",
    "Noodle powder (Wheat flour": "3.5",
    "Edible vegetable oil": "3.2",
    "Salt": "2.5",
    "Wheat gluten": "3.5",
    "Mineral (170(i)) and Guar gum)": "3.5",
    "Sugar": "3.5",
    "Edible starch": "3.5",
    "Edible vegetable oil": "3.5",
    "Acidifying agent (330)": "3.5",
    "Mineral (508)": "3.5",
    "Flavour enhancer (635)":"3.5",
    "Dextrin":"2.6",
    "Carrageenan":"2.6",
    "Cellulose Gum":"2.6",
    "Potassium Citrate":"2.6",
}
   
    return ingredientsList
