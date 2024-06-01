section .bss
        pick_input resb 1

section .data
        pick_prompt db "Rock[R], Paper[P], or Scissors[S]: ", 0

section .text
        global _start

_start:
        ; write prompt to user
        mov rax, 1      ; sys_write
        mov rdi, 1      ; file descriptor, 1 stdout(terminal)
        mov rsi, pick_prompt    ; pointer to string
        mov rdx, 35     ; amount of bytes to write
        syscall

        ; read and collect user input
        mov rax, 0      ; sys_read
        mov rdi, 1      ; stdout
        mov rsi, pick_input     ; store user input
        mov rdx, 1
        syscall

        ; exit program
        mov rax, 60     ; sys_exit
        xor rdi, rdi    ; clear rdi register and set it to 0
        syscall
