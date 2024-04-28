import * as React from "react"
import * as SelectPrimitive from "@radix-ui/react-select"
import { Check, ChevronDown, ChevronUp } from "lucide-react"

import { cn } from "@/lib/utils"

const Select = SelectPrimitive.Root

const SelectGroup = SelectPrimitive.Group

const SelectValue = SelectPrimitive.Value

const SelectTrigger = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Trigger>
>(({ className, children, ...props }, ref) => (
  <SelectPrimitive.Trigger
    ref={ref}
    className={cn(
      "ndefinedflex ndefinedh-10 ndefinedw-full ndefineditems-center ndefinedjustify-between ndefinedrounded-md ndefinedborder ndefinedborder-input ndefinedbg-background ndefinedpx-3 ndefinedpy-2 ndefinedtext-sm ndefinedring-offset-background placeholder:ndefinedtext-muted-foreground focus:ndefinedoutline-none focus:ndefinedring-2 focus:ndefinedring-ring focus:ndefinedring-offset-2 disabled:ndefinedcursor-not-allowed disabled:ndefinedopacity-50 [&>span]:ndefinedline-clamp-1",
      className
    )}
    {...props}
  >
    {children}
    <SelectPrimitive.Icon asChild>
      <ChevronDown className="ndefinedh-4 ndefinedw-4 ndefinedopacity-50" />
    </SelectPrimitive.Icon>
  </SelectPrimitive.Trigger>
))
SelectTrigger.displayName = SelectPrimitive.Trigger.displayName

const SelectScrollUpButton = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.ScrollUpButton>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.ScrollUpButton>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.ScrollUpButton
    ref={ref}
    className={cn(
      "ndefinedflex ndefinedcursor-default ndefineditems-center ndefinedjustify-center ndefinedpy-1",
      className
    )}
    {...props}
  >
    <ChevronUp className="ndefinedh-4 ndefinedw-4" />
  </SelectPrimitive.ScrollUpButton>
))
SelectScrollUpButton.displayName = SelectPrimitive.ScrollUpButton.displayName

const SelectScrollDownButton = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.ScrollDownButton>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.ScrollDownButton>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.ScrollDownButton
    ref={ref}
    className={cn(
      "ndefinedflex ndefinedcursor-default ndefineditems-center ndefinedjustify-center ndefinedpy-1",
      className
    )}
    {...props}
  >
    <ChevronDown className="ndefinedh-4 ndefinedw-4" />
  </SelectPrimitive.ScrollDownButton>
))
SelectScrollDownButton.displayName =
  SelectPrimitive.ScrollDownButton.displayName

const SelectContent = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Content>
>(({ className, children, position = "popper", ...props }, ref) => (
  <SelectPrimitive.Portal>
    <SelectPrimitive.Content
      ref={ref}
      className={cn(
        "ndefinedrelative ndefinedz-50 ndefinedmax-h-96 ndefinedmin-w-[8rem] ndefinedoverflow-hidden ndefinedrounded-md ndefinedborder ndefinedbg-popover ndefinedtext-popover-foreground ndefinedshadow-md data-[state=open]:ndefinedanimate-in data-[state=closed]:ndefinedanimate-out data-[state=closed]:ndefinedfade-out-0 data-[state=open]:ndefinedfade-in-0 data-[state=closed]:ndefinedzoom-out-95 data-[state=open]:ndefinedzoom-in-95 data-[side=bottom]:ndefinedslide-in-from-top-2 data-[side=left]:ndefinedslide-in-from-right-2 data-[side=right]:ndefinedslide-in-from-left-2 data-[side=top]:ndefinedslide-in-from-bottom-2",
        position === "popper" &&
          "data-[side=bottom]:ndefinedtranslate-y-1 data-[side=left]:ndefined-translate-x-1 data-[side=right]:ndefinedtranslate-x-1 data-[side=top]:ndefined-translate-y-1",
        className
      )}
      position={position}
      {...props}
    >
      <SelectScrollUpButton />
      <SelectPrimitive.Viewport
        className={cn(
          "ndefinedp-1",
          position === "popper" &&
            "ndefinedh-[var(--radix-select-trigger-height)] ndefinedw-full ndefinedmin-w-[var(--radix-select-trigger-width)]"
        )}
      >
        {children}
      </SelectPrimitive.Viewport>
      <SelectScrollDownButton />
    </SelectPrimitive.Content>
  </SelectPrimitive.Portal>
))
SelectContent.displayName = SelectPrimitive.Content.displayName

const SelectLabel = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Label>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.Label
    ref={ref}
    className={cn("ndefinedpy-1.5 ndefinedpl-8 ndefinedpr-2 ndefinedtext-sm ndefinedfont-semibold", className)}
    {...props}
  />
))
SelectLabel.displayName = SelectPrimitive.Label.displayName

const SelectItem = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Item>
>(({ className, children, ...props }, ref) => (
  <SelectPrimitive.Item
    ref={ref}
    className={cn(
      "ndefinedrelative ndefinedflex ndefinedw-full ndefinedcursor-default ndefinedselect-none ndefineditems-center ndefinedrounded-sm ndefinedpy-1.5 ndefinedpl-8 ndefinedpr-2 ndefinedtext-sm ndefinedoutline-none focus:ndefinedbg-accent focus:ndefinedtext-accent-foreground data-[disabled]:ndefinedpointer-events-none data-[disabled]:ndefinedopacity-50",
      className
    )}
    {...props}
  >
    <span className="ndefinedabsolute ndefinedleft-2 ndefinedflex ndefinedh-3.5 ndefinedw-3.5 ndefineditems-center ndefinedjustify-center">
      <SelectPrimitive.ItemIndicator>
        <Check className="ndefinedh-4 ndefinedw-4" />
      </SelectPrimitive.ItemIndicator>
    </span>

    <SelectPrimitive.ItemText>{children}</SelectPrimitive.ItemText>
  </SelectPrimitive.Item>
))
SelectItem.displayName = SelectPrimitive.Item.displayName

const SelectSeparator = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.Separator
    ref={ref}
    className={cn("ndefined-mx-1 ndefinedmy-1 ndefinedh-px ndefinedbg-muted", className)}
    {...props}
  />
))
SelectSeparator.displayName = SelectPrimitive.Separator.displayName

export {
  Select,
  SelectGroup,
  SelectValue,
  SelectTrigger,
  SelectContent,
  SelectLabel,
  SelectItem,
  SelectSeparator,
  SelectScrollUpButton,
  SelectScrollDownButton,
}
