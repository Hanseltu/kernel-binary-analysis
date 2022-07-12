#include <stdio.h>

int main (int artc, char** argv) {
	asm(R"(
    mov (%rdi), %rax
    mov $0, %rbx
    //mov $0, %eax
	inc %rax
	dec %ax
	
	cmovg %rax, %rbx
)");
	return 0 ;
}