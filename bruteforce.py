# -*- coding: utf-8 -*-

import csv
import datetime


def retrieve_data():
    with open("shares.csv") as shares_csv:
        next(shares_csv)
        reader = csv.reader(shares_csv, delimiter=",")
        shares_list = []
        for line in reader:
            shares_list.append({
                "name": line[0],
                "price": float(line[1]),
                "profit": (float(line[1]) * float(line[2])) / 100
            })
        return shares_list


def integer_to_binary():
    shares_list = retrieve_data()
    number_of_shares = len(shares_list)
    integer_table = [integer for integer in range(2**number_of_shares)]
    binary_table = [bin(integer)[2:] for integer in integer_table]
    combinations_table = ["0"*(number_of_shares-len(number)) + number for number in binary_table]
    return combinations_table


def generate_possible_combinations():
    shares_list = retrieve_data()
    number_of_shares = len(shares_list)
    max_spending = 500
    combinations = integer_to_binary()
    possible_combinations = []
    for combination in combinations:
        combination_price = 0
        combination_profit = 0
        combination_shares = []
        for i in range(number_of_shares):
            if combination[i] == "1":
                combination_price = combination_price + shares_list[i]["price"]
                combination_profit = combination_profit + shares_list[i]["profit"]
                combination_shares.append(shares_list[i]["name"])
        if combination_price <= max_spending:
            possible_combinations.append((combination_shares, combination_profit, combination_price))
    return possible_combinations


def generate_best_combination():
    combinations_list = generate_possible_combinations()
    shares_to_buy = combinations_list[0][0]
    max_profit = combinations_list[0][1]
    combination_price = combinations_list[0][2]
    for combination in combinations_list:
        if combination[1] > max_profit:
            shares_to_buy = combination[0]
            max_profit = combination[1]
            combination_price = combination[2]
    return shares_to_buy, combination_price, max_profit


def display_result():
    shares_to_buy, combination_price, max_profit = generate_best_combination()
    print("La solution optimale est d'acheter les actions suivantes:")
    for share in shares_to_buy:
        print("- " + share)
    print("Elle coûtera " + str(round(combination_price, 2)) + "€ et aura un profit de " + str(round(max_profit, 2)) + "€.")


if __name__ == '__main__':
    start_date = datetime.datetime.now()
    display_result()
    end_date = datetime.datetime.now()
    time = end_date - start_date
    print("Durée d'exécution de l'algorithme : " + str(time))
