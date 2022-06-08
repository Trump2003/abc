thisdict= {
    "confident":{"tu tin","lieu linh","can dam"},
    "provision":{"cung cap","du lieu","du tru"},
    "hello":{"xin chao","chao nhau"},
    "goodbye": {"tam biet" ,"loi tu biet"},
    "obligate":{"bat buoc",'ep buoc'}
}
x=thisdict
print(x)
X = len(thisdict)
print(f'times element:{X}')
y={"comsume":"tieu thu" }
thisdict.update({"comsume":"tieu thu"})
print(thisdict)
Y= thisdict.get("confident")
print(Y)
T=thisdict.get("tieu thu")
print (T)