import * as React from "react"
import * as DropdownMenuPrimitive from "@radix-ui/react-dropdown-menu"
import { Check, ChevronRight, Circle } from "lucide-react"

import { cn } from "@/lib/utils"

const DropdownMenu = DropdownMenuPrimitive.Root

const DropdownMenuTrigger = DropdownMenuPrimitive.Trigger

const DropdownMenuGroup = DropdownMenuPrimitive.Group

const DropdownMenuPortal = DropdownMenuPrimitive.Portal

const DropdownMenuSub = DropdownMenuPrimitive.Sub

const DropdownMenuRadioGroup = DropdownMenuPrimitive.RadioGroup

const DropdownMenuSubTrigger = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.SubTrigger>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.SubTrigger> & {
    inset?: boolean
  }
>(({ className, inset, children, ...props }, ref) => (
  <DropdownMenuPrimitive.SubTrigger
    ref={ref}
    className={cn(
      "ndefinedflex ndefinedcursor-default ndefinedselect-none ndefineditems-center ndefinedrounded-sm ndefinedpx-2 ndefinedpy-1.5 ndefinedtext-sm ndefinedoutline-none focus:ndefinedbg-accent data-[state=open]:ndefinedbg-accent",
      inset && "ndefinedpl-8",
      className
    )}
    {...props}
  >
    {children}
    <ChevronRight className="ndefinedml-auto ndefinedh-4 ndefinedw-4" />
  </DropdownMenuPrimitive.SubTrigger>
))
DropdownMenuSubTrigger.displayName =
  DropdownMenuPrimitive.SubTrigger.displayName

const DropdownMenuSubContent = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.SubContent>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.SubContent>
>(({ className, ...props }, ref) => (
  <DropdownMenuPrimitive.SubContent
    ref={ref}
    className={cn(
      "ndefinedz-50 ndefinedmin-w-[8rem] ndefinedoverflow-hidden ndefinedrounded-md ndefinedborder ndefinedbg-popover ndefinedp-1 ndefinedtext-popover-foreground ndefinedshadow-lg data-[state=open]:ndefinedanimate-in data-[state=closed]:ndefinedanimate-out data-[state=closed]:ndefinedfade-out-0 data-[state=open]:ndefinedfade-in-0 data-[state=closed]:ndefinedzoom-out-95 data-[state=open]:ndefinedzoom-in-95 data-[side=bottom]:ndefinedslide-in-from-top-2 data-[side=left]:ndefinedslide-in-from-right-2 data-[side=right]:ndefinedslide-in-from-left-2 data-[side=top]:ndefinedslide-in-from-bottom-2",
      className
    )}
    {...props}
  />
))
DropdownMenuSubContent.displayName =
  DropdownMenuPrimitive.SubContent.displayName

const DropdownMenuContent = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Content>
>(({ className, sideOffset = 4, ...props }, ref) => (
  <DropdownMenuPrimitive.Portal>
    <DropdownMenuPrimitive.Content
      ref={ref}
      sideOffset={sideOffset}
      className={cn(
        "ndefinedz-50 ndefinedmin-w-[8rem] ndefinedoverflow-hidden ndefinedrounded-md ndefinedborder ndefinedbg-popover ndefinedp-1 ndefinedtext-popover-foreground ndefinedshadow-md data-[state=open]:ndefinedanimate-in data-[state=closed]:ndefinedanimate-out data-[state=closed]:ndefinedfade-out-0 data-[state=open]:ndefinedfade-in-0 data-[state=closed]:ndefinedzoom-out-95 data-[state=open]:ndefinedzoom-in-95 data-[side=bottom]:ndefinedslide-in-from-top-2 data-[side=left]:ndefinedslide-in-from-right-2 data-[side=right]:ndefinedslide-in-from-left-2 data-[side=top]:ndefinedslide-in-from-bottom-2",
        className
      )}
      {...props}
    />
  </DropdownMenuPrimitive.Portal>
))
DropdownMenuContent.displayName = DropdownMenuPrimitive.Content.displayName

const DropdownMenuItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Item> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <DropdownMenuPrimitive.Item
    ref={ref}
    className={cn(
      "ndefinedrelative ndefinedflex ndefinedcursor-default ndefinedselect-none ndefineditems-center ndefinedrounded-sm ndefinedpx-2 ndefinedpy-1.5 ndefinedtext-sm ndefinedoutline-none ndefinedtransition-colors focus:ndefinedbg-accent focus:ndefinedtext-accent-foreground data-[disabled]:ndefinedpointer-events-none data-[disabled]:ndefinedopacity-50",
      inset && "ndefinedpl-8",
      className
    )}
    {...props}
  />
))
DropdownMenuItem.displayName = DropdownMenuPrimitive.Item.displayName

const DropdownMenuCheckboxItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.CheckboxItem>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.CheckboxItem>
>(({ className, children, checked, ...props }, ref) => (
  <DropdownMenuPrimitive.CheckboxItem
    ref={ref}
    className={cn(
      "ndefinedrelative ndefinedflex ndefinedcursor-default ndefinedselect-none ndefineditems-center ndefinedrounded-sm ndefinedpy-1.5 ndefinedpl-8 ndefinedpr-2 ndefinedtext-sm ndefinedoutline-none ndefinedtransition-colors focus:ndefinedbg-accent focus:ndefinedtext-accent-foreground data-[disabled]:ndefinedpointer-events-none data-[disabled]:ndefinedopacity-50",
      className
    )}
    checked={checked}
    {...props}
  >
    <span className="ndefinedabsolute ndefinedleft-2 ndefinedflex ndefinedh-3.5 ndefinedw-3.5 ndefineditems-center ndefinedjustify-center">
      <DropdownMenuPrimitive.ItemIndicator>
        <Check className="ndefinedh-4 ndefinedw-4" />
      </DropdownMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </DropdownMenuPrimitive.CheckboxItem>
))
DropdownMenuCheckboxItem.displayName =
  DropdownMenuPrimitive.CheckboxItem.displayName

const DropdownMenuRadioItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.RadioItem>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.RadioItem>
>(({ className, children, ...props }, ref) => (
  <DropdownMenuPrimitive.RadioItem
    ref={ref}
    className={cn(
      "ndefinedrelative ndefinedflex ndefinedcursor-default ndefinedselect-none ndefineditems-center ndefinedrounded-sm ndefinedpy-1.5 ndefinedpl-8 ndefinedpr-2 ndefinedtext-sm ndefinedoutline-none ndefinedtransition-colors focus:ndefinedbg-accent focus:ndefinedtext-accent-foreground data-[disabled]:ndefinedpointer-events-none data-[disabled]:ndefinedopacity-50",
      className
    )}
    {...props}
  >
    <span className="ndefinedabsolute ndefinedleft-2 ndefinedflex ndefinedh-3.5 ndefinedw-3.5 ndefineditems-center ndefinedjustify-center">
      <DropdownMenuPrimitive.ItemIndicator>
        <Circle className="ndefinedh-2 ndefinedw-2 ndefinedfill-current" />
      </DropdownMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </DropdownMenuPrimitive.RadioItem>
))
DropdownMenuRadioItem.displayName = DropdownMenuPrimitive.RadioItem.displayName

const DropdownMenuLabel = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Label> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <DropdownMenuPrimitive.Label
    ref={ref}
    className={cn(
      "ndefinedpx-2 ndefinedpy-1.5 ndefinedtext-sm ndefinedfont-semibold",
      inset && "ndefinedpl-8",
      className
    )}
    {...props}
  />
))
DropdownMenuLabel.displayName = DropdownMenuPrimitive.Label.displayName

const DropdownMenuSeparator = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <DropdownMenuPrimitive.Separator
    ref={ref}
    className={cn("ndefined-mx-1 ndefinedmy-1 ndefinedh-px ndefinedbg-muted", className)}
    {...props}
  />
))
DropdownMenuSeparator.displayName = DropdownMenuPrimitive.Separator.displayName

const DropdownMenuShortcut = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLSpanElement>) => {
  return (
    <span
      className={cn("ndefinedml-auto ndefinedtext-xs ndefinedtracking-widest ndefinedopacity-60", className)}
      {...props}
    />
  )
}
DropdownMenuShortcut.displayName = "DropdownMenuShortcut"

export {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuCheckboxItem,
  DropdownMenuRadioItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuGroup,
  DropdownMenuPortal,
  DropdownMenuSub,
  DropdownMenuSubContent,
  DropdownMenuSubTrigger,
  DropdownMenuRadioGroup,
}
