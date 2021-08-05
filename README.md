# SOM.md
Berikut adalah Implementasi Kasus sederhana Algoritma Self Organizing Map (SOM) dengan menggunakan Python.

## Metode
+ Inisialisasi parameter : 
  1. Jumlah masukan (𝑛)
  2. jumlah pola (𝑚)
  3. fungsi pembelajaran (lr)
  4. minimal learning rate (𝑚𝑖𝑛(𝛼))
  5. learning rate(𝛼).
+ Inisialisasi vektor input 𝑥1,…,𝑥𝑛
+ Membangkitkan weight (bobot) neuron output secara acak (𝑤𝑖𝑗).
+ Mencari jarak terdekat dari masing-masing neuron output ke data input, menggunakan rumus Euclidian Distance
    
      𝐷𝑖=∑(𝑤𝑖𝑗−𝑥𝑖)^2) 
	
+ Dari seluruh bobot (𝐷𝑖) dicari yang paling kecil jaraknya, indeks dari bobot (𝐷𝑖) ini disebut 	winning neuron.
+ Update bobot neuron output. Untuk semua unit j didalam ketetanggaan j dan untuk semua i,  𝒘𝒊𝒋 diperbaharui dengan menggunakan rumus berikut :

      𝒘𝒊𝒋(baru) = 𝒘𝒊𝒋(lama) + α(lama)[𝒙𝒊−𝒘𝒊𝒋(𝒍𝒂𝒎𝒂)]

+ Update learning rate. 
      
      𝜶(baru) = lr x 𝜶(lama)
      
+ Jika 𝜶 ≤ 𝒎𝒊𝒏(𝜶), stop. Sebaliknya, jika 𝜶 ≥ 𝒎𝒊𝒏(𝜶) ulangi langkah 4 sampai 7.
+ Simpan bobot neuron output terakhir.

## Authors
* **Mega Musfivawati** - *Initial work* - [megamusfiva](https://github.com/megamusfiva/)
