def genetate_tabel(n):
    tabels="" 
    for i in range(1,11):
        tabels+=f"{n} x {i} = {n*i}\n"

    with open(f"chapter9_pratice.py/tabels/tabel_{n}.txt","w") as f:
        f.write(tabels)






for i in range(2,21):
    genetate_tabel(i)