segundos_str=input("Número de segundos a converter:")
total_segs=int(segundos_str)

horas=total_segs // 3600
segs_restantes=total_segs %3600
minutos=segs_restantes//60
segs_restantes_final=segs_restantes%60
print(horas,"horas",minutos,"minutos e", segs_restantes_final,"segundos.")
