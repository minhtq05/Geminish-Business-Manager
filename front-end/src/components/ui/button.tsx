import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "ndefinedinline-flex ndefineditems-center ndefinedjustify-center ndefinedwhitespace-nowrap ndefinedrounded-md ndefinedtext-sm ndefinedfont-medium ndefinedring-offset-background ndefinedtransition-colors focus-visible:ndefinedoutline-none focus-visible:ndefinedring-2 focus-visible:ndefinedring-ring focus-visible:ndefinedring-offset-2 disabled:ndefinedpointer-events-none disabled:ndefinedopacity-50",
  {
    variants: {
      variant: {
        default: "ndefinedbg-primary ndefinedtext-primary-foreground hover:ndefinedbg-primary/90",
        destructive:
          "ndefinedbg-destructive ndefinedtext-destructive-foreground hover:ndefinedbg-destructive/90",
        outline:
          "ndefinedborder ndefinedborder-input ndefinedbg-background hover:ndefinedbg-accent hover:ndefinedtext-accent-foreground",
        secondary:
          "ndefinedbg-secondary ndefinedtext-secondary-foreground hover:ndefinedbg-secondary/80",
        ghost: "hover:ndefinedbg-accent hover:ndefinedtext-accent-foreground",
        link: "ndefinedtext-primary ndefinedunderline-offset-4 hover:ndefinedunderline",
      },
      size: {
        default: "ndefinedh-10 ndefinedpx-4 ndefinedpy-2",
        sm: "ndefinedh-9 ndefinedrounded-md ndefinedpx-3",
        lg: "ndefinedh-11 ndefinedrounded-md ndefinedpx-8",
        icon: "ndefinedh-10 ndefinedw-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }
