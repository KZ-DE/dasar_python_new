import datetime


# multi key
mahasiswa = {
    'nama' : "sudrun",
    'nim' : "1910201111",
    'skslulus' : 138,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2001,9,1)
}
tampilkan = mahasiswa.items()
for a,b in tampilkan:
    print(f"{a}  {b}")
print()
    
mahasiswa2 = {
    'nama' : "bejo",
    'nim' : "1910202222",
    'skslulus' : 138,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2002,4,12)
}
tampilkan2 = mahasiswa2.items()
for x,y in tampilkan2:
    print(f"{x}  {y}")
print()
    
mahasiswa3 = {
    'nama' : "makelah",
    'nim' : "1910202222",
    'skslulus' : 120,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2003,1,9)
}
tampilkan3 = mahasiswa3.items()
for c,d in tampilkan3:
    print(f"{c}  {d}")
print()
print("="*10+"\nDATA BASE\n"+"="*10)
data_mahasiswa = {
    'MAH001' : mahasiswa,
    'MAH002' : mahasiswa2,
    'MAH003' : mahasiswa3,
}
print(f"{'key':<6} {'nama':^16} {'sks':<3} {'beasiswa':^9} {'tanggal lahir':<10}")
# arti dari ( :<6 ) adalah membuat string rata kiri dan angak 6 adalah max huruf ke samping
# sedangkan ada format lainnya yaitu rata kanan (:>6), dan rata tengah ( :^6 )
print("-"*60)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['skslulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<16} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
