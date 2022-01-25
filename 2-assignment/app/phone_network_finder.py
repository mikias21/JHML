# Imports
from tokenize import group
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

# Load our dataset
dataset = pd.read_csv("../datasets/dataset.csv", engine='python')
# print(dataset.info()) -> Uncomment

# Show the head of the dataset
# print(dataset.head()) -> Uncomment


def count_number_of_relations(number):
    result_set = dataset.iloc[(dataset['From'] == int(number)).values]
    result_set_list = result_set.values.tolist()
    nodes = []
    for result in result_set_list:
        for item in result:
            if type(item) == int and item != int(number) and item not in nodes:
                nodes.append(item)
    return len(nodes)


def get_height(height):
    if height == 0:
        height += 20
    elif height == 1:
        height += 30
    elif height >= 2 and height < 40:
        height += 40
    return height


def get_sub_nodes(number):
    result_set = dataset.iloc[(dataset['From'] == int(number)).values]
    result_set_list = result_set.values.tolist()
    nodes = []

    for result in result_set_list:
        for item in result:
            if type(item) == int and item != int(number) and item not in nodes:
                nodes.append(item)
    return nodes


def find_phone_network(number):
    # Get all From phone numbers from our dataset for search
    result_set = dataset.iloc[(dataset['From'] == int(number)).values]
    # Build nodes and edges
    relationship = {"nodes": [], "edges": []}
    result_set_list = result_set.values.tolist()
    nodes = []

    # set default
    relationship["nodes"].append({"id": number, "group": number, "height": get_height(
        count_number_of_relations(number))})

    for result in result_set_list:
        for item in result:
            if type(item) == int and item != int(number) and item not in nodes:
                nodes.append(item)

    for node in nodes:
        height = get_height(count_number_of_relations(node))
        relationship["nodes"].append(
            {"id": node, "group": number, "height": height})
        sub_nodes = get_sub_nodes(node)
        for sub_node in sub_nodes:
            relationship["nodes"].append(
                {"id": sub_node, "group": node, "height": get_height(count_number_of_relations(sub_node))})
            relationship["edges"].append({"from": node, "to": sub_node})
        relationship["edges"].append({"from": number, "to": node})
    # print(len(relation_ship["nodes"]))
    return relationship


def get_sub_nodes(number):
    result_set = dataset.iloc[(dataset['From'] == int(number)).values]
    result_set_list = result_set.values.tolist()
    nodes = []

    for result in result_set_list:
        for item in result:
            if type(item) == int and item != int(number) and item not in nodes:
                nodes.append(item)
    return nodes


def find_phone_network_second(number):
    # Get all From phone numbers from our dataset for search
    result_set = dataset.iloc[(dataset['From'] == int(number)).values]
    # Build nodes and edges
    result_set_list = result_set.values.tolist()
    relation_ship = {'data': []}
    nodes = []

    for result in result_set_list:
        for item in result:
            if type(item) == int and item != int(number) and item not in nodes:
                nodes.append(item)

    for node in nodes:
        sub_nodes = get_sub_nodes(node)
        for sub_node in sub_nodes:
            relation_ship["data"].append([str(node), str(sub_node)])
        relation_ship["data"].append([str(number), str(node)])
    return relation_ship


find_phone_network_second("265319017229")
