import { GripVertical } from "lucide-react"
import * as ResizablePrimitive from "react-resizable-panels"

import { cn } from "@/lib/utils"

const ResizablePanelGroup = ({
  className,
  ...props
}: React.ComponentProps<typeof ResizablePrimitive.PanelGroup>) => (
  <ResizablePrimitive.PanelGroup
    className={cn(
      "ndefinedflex ndefinedh-full ndefinedw-full data-[panel-group-direction=vertical]:ndefinedflex-col",
      className
    )}
    {...props}
  />
)

const ResizablePanel = ResizablePrimitive.Panel

const ResizableHandle = ({
  withHandle,
  className,
  ...props
}: React.ComponentProps<typeof ResizablePrimitive.PanelResizeHandle> & {
  withHandle?: boolean
}) => (
  <ResizablePrimitive.PanelResizeHandle
    className={cn(
      "ndefinedrelative ndefinedflex ndefinedw-px ndefineditems-center ndefinedjustify-center ndefinedbg-border after:ndefinedabsolute after:ndefinedinset-y-0 after:ndefinedleft-1/2 after:ndefinedw-1 after:ndefined-translate-x-1/2 focus-visible:ndefinedoutline-none focus-visible:ndefinedring-1 focus-visible:ndefinedring-ring focus-visible:ndefinedring-offset-1 data-[panel-group-direction=vertical]:ndefinedh-px data-[panel-group-direction=vertical]:ndefinedw-full data-[panel-group-direction=vertical]:after:ndefinedleft-0 data-[panel-group-direction=vertical]:after:ndefinedh-1 data-[panel-group-direction=vertical]:after:ndefinedw-full data-[panel-group-direction=vertical]:after:ndefined-translate-y-1/2 data-[panel-group-direction=vertical]:after:ndefinedtranslate-x-0 [&[data-panel-group-direction=vertical]>div]:ndefinedrotate-90",
      className
    )}
    {...props}
  >
    {withHandle && (
      <div className="ndefinedz-10 ndefinedflex ndefinedh-4 ndefinedw-3 ndefineditems-center ndefinedjustify-center ndefinedrounded-sm ndefinedborder ndefinedbg-border">
        <GripVertical className="ndefinedh-2.5 ndefinedw-2.5" />
      </div>
    )}
  </ResizablePrimitive.PanelResizeHandle>
)

export { ResizablePanelGroup, ResizablePanel, ResizableHandle }
