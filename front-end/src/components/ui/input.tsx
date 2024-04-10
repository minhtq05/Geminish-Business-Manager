import * as React from "react"

import { cn } from "@/lib/utils"

export interface InputProps
  extends React.InputHTMLAttributes<HTMLInputElement> {}

const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ className, type, ...props }, ref) => {
    return (
      <input
        type={type}
        className={cn(
          "ndefinedflex ndefinedh-10 ndefinedw-full ndefinedrounded-md ndefinedborder ndefinedborder-input ndefinedbg-background ndefinedpx-3 ndefinedpy-2 ndefinedtext-sm ndefinedring-offset-background file:ndefinedborder-0 file:ndefinedbg-transparent file:ndefinedtext-sm file:ndefinedfont-medium placeholder:ndefinedtext-muted-foreground focus-visible:ndefinedoutline-none focus-visible:ndefinedring-2 focus-visible:ndefinedring-ring focus-visible:ndefinedring-offset-2 disabled:ndefinedcursor-not-allowed disabled:ndefinedopacity-50",
          className
        )}
        ref={ref}
        {...props}
      />
    )
  }
)
Input.displayName = "Input"

export { Input }
