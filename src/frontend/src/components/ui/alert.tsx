import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const alertVariants = cva(
  "ndefinedrelative ndefinedw-full ndefinedrounded-lg ndefinedborder ndefinedp-4 [&>svg~*]:ndefinedpl-7 [&>svg+div]:ndefinedtranslate-y-[-3px] [&>svg]:ndefinedabsolute [&>svg]:ndefinedleft-4 [&>svg]:ndefinedtop-4 [&>svg]:ndefinedtext-foreground",
  {
    variants: {
      variant: {
        default: "ndefinedbg-background ndefinedtext-foreground",
        destructive:
          "ndefinedborder-destructive/50 ndefinedtext-destructive dark:ndefinedborder-destructive [&>svg]:ndefinedtext-destructive",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

const Alert = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement> & VariantProps<typeof alertVariants>
>(({ className, variant, ...props }, ref) => (
  <div
    ref={ref}
    role="alert"
    className={cn(alertVariants({ variant }), className)}
    {...props}
  />
))
Alert.displayName = "Alert"

const AlertTitle = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLHeadingElement>
>(({ className, ...props }, ref) => (
  <h5
    ref={ref}
    className={cn("ndefinedmb-1 ndefinedfont-medium ndefinedleading-none ndefinedtracking-tight", className)}
    {...props}
  />
))
AlertTitle.displayName = "AlertTitle"

const AlertDescription = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLParagraphElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("ndefinedtext-sm [&_p]:ndefinedleading-relaxed", className)}
    {...props}
  />
))
AlertDescription.displayName = "AlertDescription"

export { Alert, AlertTitle, AlertDescription }
