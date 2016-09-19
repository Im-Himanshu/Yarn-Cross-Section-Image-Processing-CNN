global filename A;
scz=get(0,'ScreenSize');
figure('Position',[round(scz(1,3)/4) round(scz(1,4)/8) 700 500],'MenuBar','None','NumberTitle','off','Name','Pencil sketch Application','Resize','off');
axes('Position',[0 0 .7 1],'xtick',[],'ytick',[]);
shade=uicontrol('Style','slider','Position',[500,310 200 20],'Max',1 ,'Min',0.01,'Value',0.56,'Callback',@draw);
thresh=uicontrol('Style','slider','Position',[500,370 200 20],'Max',255,'Min',0,'Value',30,'Callback',@draw);
directory=dir('*.jpg');
files={directory.name}';
tval=uicontrol('style','text','Position',[500,340 100 20]','String','Thresh :');
line=uicontrol('style','text','Position',[500,395 100 20]','String','Line :');
uicontrol('style','text','Position',[500,455 100 20]','String','Filename:');
uicontrol('Style','popupmenu','position',[500 420 160 30],'Value',1,'String',files,'Callback',@displayfile);

    function displayfile(obj,~)
        ptr=get(obj,'value');
        filename=char(files(ptr));
        A=imread(filename);                      
        imshow(A);
    end
    function draw(~,~)
       
        sh=get(shade,'Value');
        thr=get(thresh,'Value');
        thval=strcat('Thresh :', num2str(sh));
        set(tval,'String',thval);
       
        lineval=strcat('Line :', num2str(thr));
        set(line,'String',lineval);
       if(~isempty(A))
        A=imread(filename);
        B=rgb2gray(A);


The Edge of the image is detected using the sobel edge detection method.


C3=~edge(B,'sobel','VERTICAL');
C2=~edge(B,'sobel','HORIZONTAL');
C=uint8(C3.*C2);

The image is sharpened by subtracting the blur image.

F1=uint8(imfilter(B,fspecial('unsharp')/sh));

The blending of the edge and the filtered image is done.

for m=1:size(F1,1)
    for n=1:size(F1,2)
        if(C(m,n)==0)
           F1(m,n)=B(m,n)-thr;
        end
    end
end


imshow(F1);
       end
    end
end
