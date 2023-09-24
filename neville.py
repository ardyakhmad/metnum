import tkinter as tk

def neville_interpolation(points, x):
    # Implementasikan metode Neville di sini
    n = len(points)
    Q = [[0.0] * n for _ in range(n)]

    for i in range(n):
        Q[i][0] = points[i][1]

    for i in range(1, n):
        for j in range(1, i + 1):
            Q[i][j] = ((x - points[i - j][0]) * Q[i][j - 1] - (x - points[i][0]) * Q[i - 1][j - 1]) / (points[i][0] - points[i - j][0])

    return Q[n - 1][n - 1]

# fungsi menghitung 
def calculate():
    input_data = entry_points.get() #inputkan titik menggunakan ',' dan pemisah antar titik dengan ';' Cth : 0,1;2,3;4,5 dst
    x_value = float(entry_x.get())
    points = [tuple(map(float, pair.split(','))) for pair in input_data.split(';')]
    result = neville_interpolation(points, x_value)
    result_label.config(text=f'Result: {result}')

# Membuat GUI
root = tk.Tk()
root.title('Interpolation Calculator')

label_points = tk.Label(root, text='Enter data points (x,y):')
entry_points = tk.Entry(root)
label_x = tk.Label(root, text='Enter x value:')
entry_x = tk.Entry(root)
calculate_button = tk.Button(root, text='Calculate', command=calculate)
result_label = tk.Label(root, text='Result:')

label_points.pack()
entry_points.pack()
label_x.pack()
entry_x.pack()
calculate_button.pack()
result_label.pack()

root.mainloop()
