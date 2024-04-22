import {
  Card,
  CardContent,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
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
      className={cn("lg subpixel-antialiased rounded-md", className, bgColor)}
      {...props}
    >
      <CardHeader className={cn("px-2 rounded-t-md", textColor)}>
        {typeof headerComponent === "string" ? (
          <CardTitle className="font-extrabold">{headerComponent}</CardTitle>
        ) : (
          headerComponent
        )}
      </CardHeader>
      <CardContent
        className={cn(
          "px-2 py-6",
          textColor,
          !footerComponent ? "rounded-b-md" : ""
        )}
      >
        {children}
      </CardContent>
      {footerComponent ? (
        <CardFooter className={cn("px-2 py-2 rounded-b-md")}>
          {footerComponent}
        </CardFooter>
      ) : null}
    </Card>
  );
};
export default CardUI;
