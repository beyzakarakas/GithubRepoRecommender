import tkinter
from tkinter import *
from tkinter import filedialog, ttk
import tkinter as tk

window = Tk()
window.geometry("1000x740")
window.title("Github Repository Recommender")

title = Label(text="Github Project Recommender", bg="orange", fg="white", font="Verdana 20 bold", width="60")
title.place(x=0, y=0)

listBox1 = Listbox(selectmode=tkinter.EXTENDED, width="30", height="20")
listBox1.pack(side=tk.LEFT, padx=30, pady=220)


def load_data():
    file_path = filedialog.askopenfilename()  # Dosya seçme iletişim kutusunu görüntüle
    if file_path:  # Dosya seçildiyse devam et
        data = []
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line:  # Boş satırları atla
                    # Burada satırı uygun bir şekilde parçalayın ve gerekli alanları alın
                    parts = line.split("_")
                    username = parts[0]
                    id = parts[1]
                    data.append((id, username.lower()))  # Verileri tutan bir demet oluştur
                    data.sort()
        return data
    else:
        return None


def open_file_dialog():
    data = load_data()
    if data:
        listBox1.delete(0, tk.END)  # Önceki verileri temizle
        listBox1.insert(tk.END, "ID, Username")  # Sadece başlık olarak ekle
        for item in data:
            username, id = item
            listBox1.insert(tk.END, f"{id}, {username}")  # Verileri ekle


uploadUser = Button(text="Upload User Data", width="25", height="2", bg="#e0dee0", command=open_file_dialog)
uploadUser.place(x=30, y=70)

uploadRepository = Button(text="Upload Repository Data", width="25", height="2", bg="#e0dee0", command=open_file_dialog)
uploadRepository.place(x=405, y=70)

uploadStar = Button(text="Upload Star Data", width="25", height="2", bg="#e0dee0", command=open_file_dialog)
uploadStar.place(x=780, y=70)

text1 = Label(text="Recommend Repository For : ")
text1.place(x=30, y=200)

text2 = Label(text="Filter by programming language")
text2.place(x=30, y=565)

text3 = Label(text="Distance algorithms")
text3.place(x=50, y=635)


def checkbox_durum():
    if checkbox1_var.get() == 1:
        checkbox2_var.set(0)
    elif checkbox2_var.get() == 1:
        checkbox1_var.set(0)


checkbox1_var = IntVar()
checkbox1 = Checkbutton(window, text="Pearson", variable=checkbox1_var, onvalue=1, offvalue=0, command=checkbox_durum)
checkbox1.place(x=70, y=660)

checkbox2_var = IntVar()
checkbox2 = Checkbutton(window, text="Euclidean", variable=checkbox2_var, onvalue=1, offvalue=0, command=checkbox_durum)
checkbox2.place(x=70, y=680)

text4 = Label(text="Number of Recomendations : ")
text4.place(x=30, y=710)

entry = Entry(width=5)
entry.place(x=195, y=710)

text5 = Label(text="Recommendations")
text5.place(x=700, y=200)

listBox2 = Listbox(selectmode=tkinter.EXTENDED, width="70", height="30")
listBox2.place(x=550, y=220)

kisi_yazilim_dict = {
    'hacertilbec': 'JupyterNotebook',
    'sharno': 'Python',
    'ensbsr': 'TeX',
    'EnisBerk': 'C++',
    'msapaydin': 'Python',
    'BekirZahit': 'Python',
    'AdemKerenci': 'Ruby',
    'MuhammedHasan': 'C++',
    'Zeina-T': 'C',
    'mrfarukturgut': 'Python',
    'dogukankotan': 'JupyterNotebook',
    'asaydin': 'JavaScript',
    'malisit': 'JavaScript',
    'krmbzds': 'JupyterNotebook',
    'AmmarRashed': 'JupyterNotebook',
    'OmerCinal': 'Java',
    'saxpln': 'HTML',
    'alicakmak': 'Python'
}

language_combobox = ttk.Combobox(window, values=list(set(kisi_yazilim_dict.values())))
language_combobox.place(x=30, y=600)
language_combobox.set("None")

selected_person = None


def select_person(event):
    global selected_person
    if listBox1.curselection():
        selected_person = listBox1.get(listBox1.curselection())


listBox1.bind("<<ListboxSelect>>", select_person)


def recommendGithubUser():
    if selected_person and language_combobox.get():
        selected_language = language_combobox.get()
        recommended_people = [kisi for kisi, dil in kisi_yazilim_dict.items() if
                              dil == selected_language and kisi != selected_person]
        if recommended_people:
            listBox2.delete(0, tk.END)
            for kisi in recommended_people:
                listBox2.insert(tk.END, kisi)
        else:
            listBox2.delete(0, tk.END)
            listBox2.insert(tk.END, "Öneri bulunamadı.")
    else:
        listBox2.delete(0, tk.END)
        listBox2.insert(tk.END, "Kişi veya programlama dili seçilmedi.")


recommendGithub = Button(text="Recommend Github User", width="30", height="2", bg="#e0dee0",
                         command=recommendGithubUser)
recommendGithub.place(x=230, y=480)


# Kişi ve yazılım dilleri eşleşmelerini tanımlayın
matches = {
    0: 'JupyterNotebook',
    1: 'python',
    2: 'TeX',
    3: 'C++',
    4: 'python',
    5: 'python',
    6: 'ruby',
    7: 'C++',
    8: 'C',
    9: 'python',
    10: 'JupyterNotebook',
    11: 'JavaScript',
    12: 'JavaScript',
    13: 'JupyterNotebook',
    14: 'JupyterNotebook',
    15: 'Java',
    16: 'HTML',
    17: 'python'
}

# Kişi ve önerilen GitHub depolarını eşleştirin
repositories = {
    0: 'https://github.com/MuhammedHasan/metabolitics-breast-cancer-case-study',
    1: 'https://github.com/keras-team/keras',
    2: 'https://github.com/HIPS/neural-fingerprint',
    3: 'https://github.com/tensorflow/tensorflow',
    4: 'https://github.com/Theano/Theano',
    5: 'https://github.com/HIPS/autograd',
    6: 'https://github.com/Homebrew/brew',
    7: 'https://github.com/dmlc/xgboost',
    8: 'https://github.com/torch/torch7',
    9: 'https://github.com/sherjilozair/char-rnn-tensorflow',
    10: 'https://github.com/rasbt/python-machine-learning-book',
    11: 'https://github.com/facebook/react',
    12: 'https://github.com/facebook/react-native',
    13: 'https://github.com/ageron/handson-ml',
    14: 'https://github.com/adeshpande3/LSTM-Sentiment-Analysis',
    15: 'https://github.com/ahmetaa/zemberek-nlp',
    16: 'https://github.com/facebookresearch/fastText',
    17: 'https://github.com/mnielsen/neural-networks-and-deep-learning'
}


def get_recommendations():
    # Seçilen kişinin indeksini alın
    selected_index = listBox1.curselection()[0]

    # Seçilen kişiyle eşleşen yazılım dillerini bulun
    selected_language = matches[selected_index]

    # Önerilen depoları bulun
    recommended_repos = []
    for index, language in matches.items():
        if language == selected_language and index in repositories:
            recommended_repos.append(repositories[index])

    # Önerilen depoları göster
    listBox2.delete(0, tk.END)
    listBox2.insert(tk.END, "Önerilen GitHub Depoları:")
    for repo in recommended_repos:
        listBox2.insert(tk.END, repo)


recommendRepository = Button(text="Recommend Repository", width="30", height="2", bg="#e0dee0",
                             command=get_recommendations)
recommendRepository.place(x=230, y=440)

mainloop()
