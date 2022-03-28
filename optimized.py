# -*- coding: utf-8 -*-

import csv
import datetime


def retrieve_data(data):
    with open(data) as shares_csv:
        next(shares_csv)
        reader = csv.reader(shares_csv, delimiter=",")
        shares_list = []
        for line in reader:
            shares_list.append({
                "name": line[0],
                "price": float(line[1]),
                "percentage_profit": float(line[2]),
                "profit": (float(line[1]) * float(line[2])) / 100
            })
        return shares_list


def generate_best_combination(data):
    shares_list = retrieve_data(data)
    shares_list.sort(key=lambda item: item.get("percentage_profit"), reverse=True)
    max_spending = 500
    spending = 0
    profit = 0
    optimal_combination = []
    for share in shares_list:
        if (spending + share["price"]) <= max_spending and share["price"] > 0:
            optimal_combination.append(share)
            profit += share["profit"]
            spending += share["price"]
    return optimal_combination, spending, profit


def display_result(data):
    shares_to_buy, spending, profit = generate_best_combination(data)
    print("La solution optimale est d'acheter les actions suivantes:")
    for share in shares_to_buy:
        print("- " + share["name"])
    print("Elle coûtera " + str(round(spending, 2)) + "€ et aura un profit de " + str(round(profit, 2)) + "€.")


if __name__ == '__main__':
    start_date = datetime.datetime.now()
    display_result("dataset2.csv")
    end_date = datetime.datetime.now()
    time = end_date - start_date
    print("Durée d'exécution de l'algorithme : " + str(time))
