f1(int, int):
push rbp
mov rbp, rsp
mov DWORD PTR [rbp-20], edi
mov DWORD PTR [rbp-24], esi
mov eax, DWORD PTR [rbp-20]
mov DWORD PTR [rbp-4], eax
mov eax, DWORD PTR [rbp-4]
add DWORD PTR [rbp-20], eax
mov eax, DWORD PTR [rbp-24]
add DWORD PTR [rbp-20], eax
mov eax, DWORD PTR [rbp-20]
pop rbp
ret
main:
push rbp
mov rbp, rsp
sub rsp, 32
mov DWORD PTR [rbp-4], 100
mov DWORD PTR [rbp-32], 1
mov DWORD PTR [rbp-28], 2
mov DWORD PTR [rbp-24], 3
mov DWORD PTR [rbp-20], 4
mov DWORD PTR [rbp-16], 5
mov edx, DWORD PTR [rbp-32]
mov eax, DWORD PTR [rbp-4]
mov esi, edx
mov edi, eax
call f1(int, int)
mov DWORD PTR [rbp-4], eax
mov eax, 0
leave
ret
