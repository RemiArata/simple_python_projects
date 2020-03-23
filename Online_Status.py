def status(d):
    return(list(d.values()).count("Online"))

dtc = {
    "Remi" : "Online",
    "Suzy" : "Online",
    "Bill" : "Offline",
    "Alise" : "Online"
}

print(status(dtc))