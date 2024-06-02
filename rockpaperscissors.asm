section .bss
        pick_input resb 1
        bot_pick resb 1

section .data
        pick_prompt db "Rock[R], Paper[P], or Scissors[S]: ", 0
        is_draw db "Draw", 0
        win db "W", 0
        lose db "L", 0

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
        mov rdx, 1      ; amount of bytes to read
        syscall

        call gen_bot_pick

        call gen_winner

        ; exit program
        mov rax, 60     ; sys_exit
        xor rdi, rdi    ; clear rdi register and set it to 0
        syscall

gen_bot_pick:
        ; Generate a random number between 0 and 2
        rdrand rax
        and rax, 0x3    ; mask to keep the last two bits(0,1,2)

        cmp rax, 0      ; if rock, go to rock
        je rock
        cmp rax, 1      ; if paper, go to paper
        je paper
        jmp scissors    ; else, go to scissors

rock:
        mov byte [bot_pick], 'r'
        ret

paper:
        mov byte [bot_pick], 'p'
        ret

scissors:
        mov byte [bot_pick], 's'
        ret

gen_winner:
        mov rax, [pick_input]   ; user pick
        mov rbx, [bot_pick]     ; bot pick

        cmp rax, rbx    ; are both picks the same?
        je draw

        cmp rax, 'r'    ; is user rock?
        je user_rock

        cmp rax, 'p'    ; is user paper?
        je user_paper

        cmp rax, 's'    ; is user scissors?
        je user_scissors

user_rock:
        cmp rbx, 's'    ; is bot pick scissors?
        je user_wins
        jmp bot_wins    ; else bot wins

user_paper:
        cmp rbx, 'r'    ; is bot pick rock?
        je user_wins
        jmp bot_wins    ; else bot wins

user_scissors:
        cmp rbx, 'p'    ; is bot pick paper?
        je user_wins
        jmp bot_wins    ; else bot wins

draw:
        mov rax, 1      ; sys_write
        mov rdi, 1      ; file descriptor, stdout
        mov rsi, is_draw        ; pointer to string
        mov rdx, 4      ; length of bytes to write
        syscall
        ret             ; return

user_wins:
        mov rax, 1      ; sys_write
        mov rdi, 1      ; file descriptor, stdout
        mov rsi, win    ; pointer to string
        mov rdx, 1      ; length of bytes to write
        syscall
        ret             ; return

bot_wins:
        mov rax, 1      ; sys_write
        mov rdi, 1      ; file descriptor, stdout
        mov rsi, lose   ; pointer to string
        mov rdx, 1      ; length of bytes to write
        syscall
        ret             ; return
