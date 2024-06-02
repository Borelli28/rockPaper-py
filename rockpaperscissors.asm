section .bss
        pick_input resb 1
        bot_pick resb 1

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

        call gen_bot_pick

        ; exit program
        mov rax, 60     ; sys_exit
        xor rdi, rdi    ; clear rdi register and set it to 0
        syscall

gen_bot_pick:
        ; Generate a random number between 0 and 2
        rdrand rax
        and rax, 0x3    ; Mask to keep the last two bits(0,1,2)

        cmp rax, 0
        je rock
        cmp rax, 1
        je paper
        jmp scissors

rock:
        mov byte [bot_pick], 'r'
        ret

paper:
        mov byte [bot_pick], 'p'
        ret

scissors:
        mov byte [bot_pick], 's'
        ret
