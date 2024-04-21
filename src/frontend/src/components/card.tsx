import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { Button } from "./ui/button";
import { cn } from "@/lib/utils";
import React from "react";
interface CardUIProps {
  headerComponent: React.ReactNode;
  className?: string;
  children?: React.ReactNode | React.ReactNode[];
  footerComponent?: React.ReactNode | string;
  props?: React.ComponentPropsWithoutRef<"div">;
  colorScheme?: {
    bgColor: string | "text-current";
    textColor: string | "bg-current";
  };
}

const CardUI: React.FC<CardUIProps> = ({
  headerComponent,
  children,
  className,
  colorScheme,
  footerComponent,
  ...props
}: CardUIProps) => {
  const { bgColor, textColor } = colorScheme
    ? colorScheme
    : { bgColor: "text-current", textColor: "bg-current" };
  return (
    <Card
      className={cn(
        "drop-shadow-lg subpixel-antialiased rounded-md",
        className
      )}
      {...props}
    >
      <CardHeader className={cn("px-2 rounded-t-md", bgColor, textColor)}>
        {typeof headerComponent === "string" ? <CardTitle>{headerComponent}</CardTitle> : headerComponent}
      </CardHeader>
      <CardContent className={cn("px-2 py-10", bgColor, textColor)}>
        {children}
      </CardContent>
      <CardFooter className={cn("px-2 py-2 rounded-b-md", bgColor)}>
        {footerComponent}
      </CardFooter>
    </Card>
  );
};
export default CardUI;
