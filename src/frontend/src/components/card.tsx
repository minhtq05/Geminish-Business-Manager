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
      <CardHeader className={cn("rounded-t-md", bgColor)}>
        {typeof headerComponent === 'string' ? <CardTitle className={cn("text-4xl", textColor)}>{headerComponent}</CardTitle> : headerComponent}
      </CardHeader>
      <CardContent className={cn("py-10 rounded-b-md", bgColor, textColor)}>
        {children}
      </CardContent>
      {typeof footerComponent === "string" ? <CardFooter className={cn("rounded-t-md", bgColor, textColor)}>{footerComponent}</CardFooter> : footerComponent}
    </Card>
  );
};
export default CardUI;
