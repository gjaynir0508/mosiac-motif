import tkinter as tk


def find_motif_in_mosaic(rp, cp, motif, rq, cq, mosaic):
    matches = []
    for r in range(rq - rp + 1):
        for c in range(cq - cp + 1):
            match = True
            for i in range(rp):
                for j in range(cp):
                    if motif[i][j] != 0 and motif[i][j] != mosaic[r + i][c + j]:
                        match = False
                        break
                if not match:
                    break
            if match:
                matches.append((r + 1, c + 1))
    return matches


def on_submit():
    rp, cp = int(motif_rows_entry.get()), int(motif_cols_entry.get())
    motif = []
    for r in range(rp):
        row = []
        for c in range(cp):
            color = int(motif_cells[r][c].get())
            row.append(color)
        motif.append(row)

    rq, cq = int(mosaic_rows_entry.get()), int(mosaic_cols_entry.get())
    mosaic = []
    for r in range(rq):
        row = []
        for c in range(cq):
            color = int(mosaic_cells[r][c].get())
            row.append(color)
        mosaic.append(row)

    # Find motif matches in the mosaic
    matches = find_motif_in_mosaic(rp, cp, motif, rq, cq, mosaic)

    # Update the output text
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, f"{len(matches)}\n")
    for match in matches:
        output_text.insert(tk.END, f"{match[0]} {match[1]}\n")


# Create the main window
root = tk.Tk()
root.title("Motif Matcher")

# Motif input section
motif_frame = tk.Frame(root)
motif_frame.pack()

tk.Label(motif_frame, text="Motif Rows:").grid(row=0, column=0)
tk.Label(motif_frame, text="Motif Cols:").grid(row=1, column=0)

motif_rows_entry = tk.Entry(motif_frame)
motif_rows_entry.grid(row=0, column=1)
motif_cols_entry = tk.Entry(motif_frame)
motif_cols_entry.grid(row=1, column=1)

motif_cells_frame = tk.Frame(root)
motif_cells_frame.pack()

motif_cells = []
for r in range(5):
    row = []
    for c in range(5):
        cell = tk.Entry(motif_cells_frame, width=5)
        cell.grid(row=r, column=c)
        row.append(cell)
    motif_cells.append(row)

# Mosaic input section
mosaic_frame = tk.Frame(root)
mosaic_frame.pack()

tk.Label(mosaic_frame, text="Mosaic Rows:").grid(row=0, column=0)
tk.Label(mosaic_frame, text="Mosaic Cols:").grid(row=1, column=0)

mosaic_rows_entry = tk.Entry(mosaic_frame)
mosaic_rows_entry.grid(row=0, column=1)
mosaic_cols_entry = tk.Entry(mosaic_frame)
mosaic_cols_entry.grid(row=1, column=1)

mosaic_cells_frame = tk.Frame(root)
mosaic_cells_frame.pack()

mosaic_cells = []
for r in range(10):
    row = []
    for c in range(10):
        cell = tk.Entry(mosaic_cells_frame, width=5)
        cell.grid(row=r, column=c)
        row.append(cell)
    mosaic_cells.append(row)

# Submit button
submit_button = tk.Button(root, text="Find Matches", command=on_submit)
submit_button.pack()

# Output section
output_frame = tk.Frame(root)
output_frame.pack()

output_text = tk.Text(output_frame, height=5, width=40)
output_text.pack()

root.mainloop()
