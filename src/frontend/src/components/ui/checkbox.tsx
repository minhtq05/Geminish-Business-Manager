import * as React from "react"
import * as CheckboxPrimitive from "@radix-ui/react-checkbox"
import { Check } from "lucide-react"

import { cn } from "@/lib/utils"

const Checkbox = React.forwardRef<
  React.ElementRef<typeof CheckboxPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof CheckboxPrimitive.Root>
>(({ className, ...props }, ref) => (
  <CheckboxPrimitive.Root
    ref={ref}
    className={cn(
      "ndefinedpeer ndefinedh-4 ndefinedw-4 ndefinedshrink-0 ndefinedrounded-sm ndefinedborder ndefinedborder-primary ndefinedring-offset-background focus-visible:ndefinedoutline-none focus-visible:ndefinedring-2 focus-visible:ndefinedring-ring focus-visible:ndefinedring-offset-2 disabled:ndefinedcursor-not-allowed disabled:ndefinedopacity-50 data-[state=checked]:ndefinedbg-primary data-[state=checked]:ndefinedtext-primary-foreground",
      className
    )}
    {...props}
  >
    <CheckboxPrimitive.Indicator
      className={cn("ndefinedflex ndefineditems-center ndefinedjustify-center ndefinedtext-current")}
    >
      <Check className="ndefinedh-4 ndefinedw-4" />
    </CheckboxPrimitive.Indicator>
  </CheckboxPrimitive.Root>
))
Checkbox.displayName = CheckboxPrimitive.Root.displayName

export { Checkbox }
