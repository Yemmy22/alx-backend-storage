#!/usr/bin/env python3
'''
A log_stat function module
'''

from pymongo import MongoClient


def log_stats():
    """
    Returns stats of the nginx log in the database
    """
    client = MongoClient()
    db = client.logs
    nginx_collection = db.nginx

    total_logs = nginx_collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {
        method: nginx_collection.count_documents(
            {"method": method}
        ) for method in methods
    }

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check} status check")

    print("IPs:")
    top_ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
