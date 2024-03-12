from flask import Flask, Response, stream_with_context
import time
import uuid
import random

APP = Flask(__name__)


@APP.route("/fetch_employee_data/<int:rowcount>", methods=["GET"])
def get_large_request(rowcount):
    """returns N rows of data"""
    def f():
        for _i in range(rowcount):
            time.sleep(.001)
            id = _i+1
            occupation = random.choice(['HR Manager', 'Software Engineer', 'AI Engineer', 'BI Analyst', 'Mobile Developer', 'QA Engineer'])
            salary = random.randint(100000, 750000)
            level = random.choice(['Junior', 'Intermediate', 'Senior'])
            paid_vacation = random.choice([True, False])
            happiness = random.randint(3, 5) if (salary > 450000) & (level in ['Intermediate', 'Senior']) & (paid_vacation == True) else random.randint(1, 2)
            yield f"({id}, '{occupation}', {salary}, '{level}', '{paid_vacation}', {happiness})\n"
    return Response(stream_with_context(f()))

if __name__ == "__main__":
    APP.run(debug=True)