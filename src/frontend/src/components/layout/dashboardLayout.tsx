import React from "react";
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable";
import Sidebar from "../sidebar";
interface DashboardLayoutProps {
  children: React.ReactNode;
}
const DashboardLayout: React.FC<DashboardLayoutProps> = ({
  children,
}: DashboardLayoutProps) => {
  return (
    <ResizablePanelGroup direction="horizontal">
      <ResizablePanel
        defaultSize={25}
        className="min-w-[fit-content] max-w-[40dvw] relative h-full"
      >
        <Sidebar />
      </ResizablePanel>
      <ResizableHandle />
      <ResizablePanel defaultSize={75} className="min-w-[fit-content] ">
        {children}
      </ResizablePanel>
    </ResizablePanelGroup>
  );
};
export default DashboardLayout;
