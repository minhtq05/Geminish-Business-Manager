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
        className="min-w-[fit-content] md:max-w-[fit-content + 10dvw] relative h-full"
      >
        <Sidebar />
      </ResizablePanel>
      <ResizableHandle withHandle />
      <ResizablePanel
        defaultSize={75}
        className="min-w-[fit-content] overflow-x-hidden overflow-y-auto h-full "
      >
        {children}
      </ResizablePanel>
    </ResizablePanelGroup>
  );
};
export default DashboardLayout;
