import sys
import mysql.connector
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

print("Python:", sys.executable, flush=True)
print("Starting Dashboard...", flush=True)

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="Ctmz2020@",
        database="employee_db",
        connection_timeout=30
    )

    print("Connected to MySQL", flush=True)

    cursor = conn.cursor()

    fig = plt.figure(figsize=(18, 12))
    fig.suptitle(
        "Employee Attrition Analytics Dashboard",
        fontsize=20,
        fontweight="bold",
        y=0.98
    )

    gs = gridspec.GridSpec(
        2, 3,
        figure=fig,
        hspace=0.45,
        wspace=0.35
    )

    # Chart 1 - Overall Attrition

    cursor.execute("""
        SELECT LeaveOrNot, COUNT(*)
        FROM employees
        GROUP BY LeaveOrNot
    """)

    data = dict(cursor.fetchall())

    labels = ["Stayed", "Left"]
    sizes = [data.get(0, 0), data.get(1, 0)]

    ax1 = fig.add_subplot(gs[0, 0])

    ax1.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    ax1.set_title("Overall Attrition Rate")

    print("Chart 1 Complete", flush=True)

    # Chart 2 - Attrition by City

    cursor.execute("""
        SELECT
            City,
            ROUND(SUM(LeaveOrNot) / COUNT(*) * 100, 1)
        FROM employees
        GROUP BY City
        ORDER BY City
    """)

    rows = cursor.fetchall()

    cities = [r[0] for r in rows]
    rates = [r[1] for r in rows]

    ax2 = fig.add_subplot(gs[0, 1])

    ax2.bar(cities, rates)

    ax2.set_title("Attrition by City")
    ax2.set_ylabel("Attrition %")

    print("Chart 2 Complete", flush=True)

    # Chart 3 - Education

    cursor.execute("""
        SELECT
            Education,
            ROUND(SUM(LeaveOrNot) / COUNT(*) * 100, 1)
        FROM employees
        GROUP BY Education
        ORDER BY Education
    """)

    rows = cursor.fetchall()

    education = [r[0] for r in rows]
    rates = [r[1] for r in rows]

    ax3 = fig.add_subplot(gs[0, 2])

    ax3.barh(education, rates)

    ax3.set_title("Attrition by Education")

    print("Chart 3 Complete", flush=True)

    # Chart 4 - Gender

    cursor.execute("""
        SELECT
            Gender,
            ROUND(SUM(LeaveOrNot) / COUNT(*) * 100, 1)
        FROM employees
        GROUP BY Gender
    """)

    rows = cursor.fetchall()

    genders = [r[0] for r in rows]
    rates = [r[1] for r in rows]

    ax4 = fig.add_subplot(gs[1, 0])

    ax4.bar(genders, rates)

    ax4.set_title("Attrition by Gender")

    print("Chart 4 Complete", flush=True)

    # Chart 5 - Payment Tier

    cursor.execute("""
        SELECT
            PaymentTier,
            ROUND(SUM(LeaveOrNot) / COUNT(*) * 100, 1)
        FROM employees
        GROUP BY PaymentTier
        ORDER BY PaymentTier
    """)

    rows = cursor.fetchall()

    tiers = [str(r[0]) for r in rows]
    rates = [r[1] for r in rows]

    ax5 = fig.add_subplot(gs[1, 1])

    ax5.bar(tiers, rates)

    ax5.set_title("Attrition by Payment Tier")

    print("Chart 5 Complete", flush=True)

    # Chart 6 - Experience

    cursor.execute("""
        SELECT
            ExperienceInCurrentDomain,
            ROUND(SUM(LeaveOrNot) / COUNT(*) * 100, 1)
        FROM employees
        GROUP BY ExperienceInCurrentDomain
        ORDER BY ExperienceInCurrentDomain
    """)

    rows = cursor.fetchall()

    exp = [r[0] for r in rows]
    rates = [r[1] for r in rows]

    ax6 = fig.add_subplot(gs[1, 2])

    ax6.plot(exp, rates, marker="o")

    ax6.set_title("Attrition by Experience")

    print("Chart 6 Complete", flush=True)

    # -------------------------------------------------

    plt.savefig(
        "attrition_dashboard.png",
        dpi=150,
        bbox_inches="tight"
    )

    print(
        "Dashboard saved as attrition_dashboard.png",
        flush=True
    )

    cursor.close()
    conn.close()

    print("SUCCESS", flush=True)

except Exception as e:
    print("ERROR:", flush=True)
    print(type(e).__name__, flush=True)
    print(e, flush=True)
